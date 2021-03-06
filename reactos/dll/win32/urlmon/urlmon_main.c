/*
 * UrlMon
 *
 * Copyright (c) 2000 Patrik Stridvall
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

//#include <stdarg.h>

#include "urlmon_main.h"

//#include "winreg.h"

#define NO_SHLWAPI_REG
//#include "shlwapi.h"
#include <advpub.h>
#include <initguid.h>

#include <wine/debug.h>

#include "urlmon.h"

WINE_DEFAULT_DEBUG_CHANNEL(urlmon);

DEFINE_GUID(CLSID_CUri, 0xDF2FCE13, 0x25EC, 0x45BB, 0x9D,0x4C, 0xCE,0xCD,0x47,0xC2,0x43,0x0C);

LONG URLMON_refCount = 0;
HINSTANCE urlmon_instance;

static HMODULE hCabinet = NULL;
static DWORD urlmon_tls = TLS_OUT_OF_INDEXES;

static void init_session(void);

static struct list tls_list = LIST_INIT(tls_list);

static CRITICAL_SECTION tls_cs;
static CRITICAL_SECTION_DEBUG tls_cs_dbg =
{
    0, 0, &tls_cs,
    { &tls_cs_dbg.ProcessLocksList, &tls_cs_dbg.ProcessLocksList },
      0, 0, { (DWORD_PTR)(__FILE__ ": tls") }
};

static CRITICAL_SECTION tls_cs = { &tls_cs_dbg, -1, 0, 0, 0, 0 };

tls_data_t *get_tls_data(void)
{
    tls_data_t *data;

    if(urlmon_tls == TLS_OUT_OF_INDEXES) {
        DWORD tls = TlsAlloc();
        if(tls == TLS_OUT_OF_INDEXES)
            return NULL;

        tls = InterlockedCompareExchange((LONG*)&urlmon_tls, tls, TLS_OUT_OF_INDEXES);
        if(tls != urlmon_tls)
            TlsFree(tls);
    }

    data = TlsGetValue(urlmon_tls);
    if(!data) {
        data = heap_alloc_zero(sizeof(tls_data_t));
        if(!data)
            return NULL;

        EnterCriticalSection(&tls_cs);
        list_add_tail(&tls_list, &data->entry);
        LeaveCriticalSection(&tls_cs);

        TlsSetValue(urlmon_tls, data);
    }

    return data;
}

static void free_tls_list(void)
{
    tls_data_t *data;

    if(urlmon_tls == TLS_OUT_OF_INDEXES)
        return;

    while(!list_empty(&tls_list)) {
        data = LIST_ENTRY(list_head(&tls_list), tls_data_t, entry);
        list_remove(&data->entry);
        heap_free(data);
    }

    TlsFree(urlmon_tls);
}

static void detach_thread(void)
{
    tls_data_t *data;

    if(urlmon_tls == TLS_OUT_OF_INDEXES)
        return;

    data = TlsGetValue(urlmon_tls);
    if(!data)
        return;

    EnterCriticalSection(&tls_cs);
    list_remove(&data->entry);
    LeaveCriticalSection(&tls_cs);

    if(data->notif_hwnd) {
        WARN("notif_hwnd not destroyed\n");
        DestroyWindow(data->notif_hwnd);
    }

    heap_free(data);
}

static void process_detach(void)
{
    HINTERNET internet_session;

    internet_session = get_internet_session(NULL);
    if(internet_session)
        InternetCloseHandle(internet_session);

    if (hCabinet)
        FreeLibrary(hCabinet);

    free_session();
    free_tls_list();
}

/***********************************************************************
 *		DllMain (URLMON.init)
 */
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID fImpLoad)
{
    TRACE("%p 0x%x %p\n", hinstDLL, fdwReason, fImpLoad);

    URLMON_DllMain( hinstDLL, fdwReason, fImpLoad );

    switch(fdwReason) {
    case DLL_PROCESS_ATTACH:
        urlmon_instance = hinstDLL;
        init_session();
        break;

    case DLL_PROCESS_DETACH:
        process_detach();
        DeleteCriticalSection(&tls_cs);
        break;

    case DLL_THREAD_DETACH:
        detach_thread();
        break;
    }
    return TRUE;
}

const char *debugstr_bindstatus(ULONG status)
{
    switch(status) {
#define X(x) case x: return #x
    X(BINDSTATUS_FINDINGRESOURCE);
    X(BINDSTATUS_CONNECTING);
    X(BINDSTATUS_REDIRECTING);
    X(BINDSTATUS_BEGINDOWNLOADDATA);
    X(BINDSTATUS_DOWNLOADINGDATA);
    X(BINDSTATUS_ENDDOWNLOADDATA);
    X(BINDSTATUS_BEGINDOWNLOADCOMPONENTS);
    X(BINDSTATUS_INSTALLINGCOMPONENTS);
    X(BINDSTATUS_ENDDOWNLOADCOMPONENTS);
    X(BINDSTATUS_USINGCACHEDCOPY);
    X(BINDSTATUS_SENDINGREQUEST);
    X(BINDSTATUS_CLASSIDAVAILABLE);
    X(BINDSTATUS_MIMETYPEAVAILABLE);
    X(BINDSTATUS_CACHEFILENAMEAVAILABLE);
    X(BINDSTATUS_BEGINSYNCOPERATION);
    X(BINDSTATUS_ENDSYNCOPERATION);
    X(BINDSTATUS_BEGINUPLOADDATA);
    X(BINDSTATUS_UPLOADINGDATA);
    X(BINDSTATUS_ENDUPLOADINGDATA);
    X(BINDSTATUS_PROTOCOLCLASSID);
    X(BINDSTATUS_ENCODING);
    X(BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE);
    X(BINDSTATUS_CLASSINSTALLLOCATION);
    X(BINDSTATUS_DECODING);
    X(BINDSTATUS_LOADINGMIMEHANDLER);
    X(BINDSTATUS_CONTENTDISPOSITIONATTACH);
    X(BINDSTATUS_FILTERREPORTMIMETYPE);
    X(BINDSTATUS_CLSIDCANINSTANTIATE);
    X(BINDSTATUS_IUNKNOWNAVAILABLE);
    X(BINDSTATUS_DIRECTBIND);
    X(BINDSTATUS_RAWMIMETYPE);
    X(BINDSTATUS_PROXYDETECTING);
    X(BINDSTATUS_ACCEPTRANGES);
    X(BINDSTATUS_COOKIE_SENT);
    X(BINDSTATUS_COMPACT_POLICY_RECEIVED);
    X(BINDSTATUS_COOKIE_SUPPRESSED);
    X(BINDSTATUS_COOKIE_STATE_UNKNOWN);
    X(BINDSTATUS_COOKIE_STATE_ACCEPT);
    X(BINDSTATUS_COOKIE_STATE_REJECT);
    X(BINDSTATUS_COOKIE_STATE_PROMPT);
    X(BINDSTATUS_COOKIE_STATE_LEASH);
    X(BINDSTATUS_COOKIE_STATE_DOWNGRADE);
    X(BINDSTATUS_POLICY_HREF);
    X(BINDSTATUS_P3P_HEADER);
    X(BINDSTATUS_SESSION_COOKIE_RECEIVED);
    X(BINDSTATUS_PERSISTENT_COOKIE_RECEIVED);
    X(BINDSTATUS_SESSION_COOKIES_ALLOWED);
    X(BINDSTATUS_CACHECONTROL);
    X(BINDSTATUS_CONTENTDISPOSITIONFILENAME);
    X(BINDSTATUS_MIMETEXTPLAINMISMATCH);
    X(BINDSTATUS_PUBLISHERAVAILABLE);
    X(BINDSTATUS_DISPLAYNAMEAVAILABLE);
#undef X
    default:
        return wine_dbg_sprintf("(invalid status %u)", status);
    }
}

/***********************************************************************
 *		DllInstall (URLMON.@)
 */
HRESULT WINAPI DllInstall(BOOL bInstall, LPCWSTR cmdline)
{
  FIXME("(%s, %s): stub\n", bInstall?"TRUE":"FALSE",
	debugstr_w(cmdline));

  return S_OK;
}

/***********************************************************************
 *		DllCanUnloadNow (URLMON.@)
 */
HRESULT WINAPI DllCanUnloadNow(void)
{
    return URLMON_refCount != 0 ? S_FALSE : S_OK;
}



/******************************************************************************
 * Urlmon ClassFactory
 */
typedef struct {
    IClassFactory IClassFactory_iface;

    HRESULT (*pfnCreateInstance)(IUnknown *pUnkOuter, LPVOID *ppObj);
} ClassFactory;

static inline ClassFactory *impl_from_IClassFactory(IClassFactory *iface)
{
    return CONTAINING_RECORD(iface, ClassFactory, IClassFactory_iface);
}

static HRESULT WINAPI CF_QueryInterface(IClassFactory *iface, REFIID riid, LPVOID *ppv)
{
    *ppv = NULL;

    if(IsEqualGUID(riid, &IID_IUnknown)) {
        TRACE("(%p)->(IID_IUnknown %p)\n", iface, ppv);
        *ppv = iface;
    }else if(IsEqualGUID(riid, &IID_IClassFactory)) {
        TRACE("(%p)->(IID_IClassFactory %p)\n", iface, ppv);
        *ppv = iface;
    }

    if(*ppv) {
	IUnknown_AddRef((IUnknown*)*ppv);
	return S_OK;
    }

    WARN("(%p)->(%s,%p),not found\n", iface, debugstr_guid(riid), ppv);
    return E_NOINTERFACE;
}

static ULONG WINAPI CF_AddRef(IClassFactory *iface)
{
    URLMON_LockModule();
    return 2;
}

static ULONG WINAPI CF_Release(IClassFactory *iface)
{
    URLMON_UnlockModule();
    return 1;
}


static HRESULT WINAPI CF_CreateInstance(IClassFactory *iface, IUnknown *pOuter,
                                        REFIID riid, LPVOID *ppobj)
{
    ClassFactory *This = impl_from_IClassFactory(iface);
    HRESULT hres;
    LPUNKNOWN punk;
    
    TRACE("(%p)->(%p,%s,%p)\n",This,pOuter,debugstr_guid(riid),ppobj);

    *ppobj = NULL;
    if(SUCCEEDED(hres = This->pfnCreateInstance(pOuter, (LPVOID *) &punk))) {
        hres = IUnknown_QueryInterface(punk, riid, ppobj);
        IUnknown_Release(punk);
    }
    return hres;
}

static HRESULT WINAPI CF_LockServer(LPCLASSFACTORY iface,BOOL dolock)
{
    TRACE("(%d)\n", dolock);

    if (dolock)
	   URLMON_LockModule();
    else
	   URLMON_UnlockModule();

    return S_OK;
}

static const IClassFactoryVtbl ClassFactoryVtbl =
{
    CF_QueryInterface,
    CF_AddRef,
    CF_Release,
    CF_CreateInstance,
    CF_LockServer
};

static ClassFactory FileProtocolCF =
    { { &ClassFactoryVtbl }, FileProtocol_Construct};
static ClassFactory FtpProtocolCF =
    { { &ClassFactoryVtbl }, FtpProtocol_Construct};
static ClassFactory GopherProtocolCF =
    { { &ClassFactoryVtbl }, GopherProtocol_Construct};
static ClassFactory HttpProtocolCF =
    { { &ClassFactoryVtbl }, HttpProtocol_Construct};
static ClassFactory HttpSProtocolCF =
    { { &ClassFactoryVtbl }, HttpSProtocol_Construct};
static ClassFactory MkProtocolCF =
    { { &ClassFactoryVtbl }, MkProtocol_Construct};
static ClassFactory SecurityManagerCF =
    { { &ClassFactoryVtbl }, SecManagerImpl_Construct};
static ClassFactory ZoneManagerCF =
    { { &ClassFactoryVtbl }, ZoneMgrImpl_Construct};
static ClassFactory StdURLMonikerCF =
    { { &ClassFactoryVtbl }, StdURLMoniker_Construct};
static ClassFactory MimeFilterCF =
    { { &ClassFactoryVtbl }, MimeFilter_Construct};
static ClassFactory CUriCF =
    { { &ClassFactoryVtbl }, Uri_Construct};

struct object_creation_info
{
    const CLSID *clsid;
    IClassFactory *cf;
    LPCWSTR protocol;
};

static const WCHAR wszFile[] = {'f','i','l','e',0};
static const WCHAR wszFtp[]  = {'f','t','p',0};
static const WCHAR wszGopher[]  = {'g','o','p','h','e','r',0};
static const WCHAR wszHttp[] = {'h','t','t','p',0};
static const WCHAR wszHttps[] = {'h','t','t','p','s',0};
static const WCHAR wszMk[]   = {'m','k',0};

static const struct object_creation_info object_creation[] =
{
    { &CLSID_FileProtocol,            &FileProtocolCF.IClassFactory_iface,    wszFile },
    { &CLSID_FtpProtocol,             &FtpProtocolCF.IClassFactory_iface,     wszFtp  },
    { &CLSID_GopherProtocol,          &GopherProtocolCF.IClassFactory_iface,  wszGopher },
    { &CLSID_HttpProtocol,            &HttpProtocolCF.IClassFactory_iface,    wszHttp },
    { &CLSID_HttpSProtocol,           &HttpSProtocolCF.IClassFactory_iface,   wszHttps },
    { &CLSID_MkProtocol,              &MkProtocolCF.IClassFactory_iface,      wszMk },
    { &CLSID_InternetSecurityManager, &SecurityManagerCF.IClassFactory_iface, NULL    },
    { &CLSID_InternetZoneManager,     &ZoneManagerCF.IClassFactory_iface,     NULL    },
    { &CLSID_StdURLMoniker,           &StdURLMonikerCF.IClassFactory_iface,   NULL    },
    { &CLSID_DeCompMimeFilter,        &MimeFilterCF.IClassFactory_iface,      NULL    },
    { &CLSID_CUri,                    &CUriCF.IClassFactory_iface,            NULL    }
};

static void init_session(void)
{
    unsigned int i;

    for(i=0; i < sizeof(object_creation)/sizeof(object_creation[0]); i++) {
        if(object_creation[i].protocol)
            register_namespace(object_creation[i].cf, object_creation[i].clsid,
                                      object_creation[i].protocol, TRUE);
    }
}

/*******************************************************************************
 * DllGetClassObject [URLMON.@]
 * Retrieves class object from a DLL object
 *
 * NOTES
 *    Docs say returns STDAPI
 *
 * PARAMS
 *    rclsid [I] CLSID for the class object
 *    riid   [I] Reference to identifier of interface for class object
 *    ppv    [O] Address of variable to receive interface pointer for riid
 *
 * RETURNS
 *    Success: S_OK
 *    Failure: CLASS_E_CLASSNOTAVAILABLE, E_OUTOFMEMORY, E_INVALIDARG,
 *             E_UNEXPECTED
 */

HRESULT WINAPI DllGetClassObject(REFCLSID rclsid, REFIID riid, LPVOID *ppv)
{
    unsigned int i;
    HRESULT hr;
    
    TRACE("(%s,%s,%p)\n", debugstr_guid(rclsid), debugstr_guid(riid), ppv);
    
    for (i=0; i < sizeof(object_creation)/sizeof(object_creation[0]); i++)
    {
	if (IsEqualGUID(object_creation[i].clsid, rclsid))
	    return IClassFactory_QueryInterface(object_creation[i].cf, riid, ppv);
    }

    hr = URLMON_DllGetClassObject(rclsid, riid, ppv);
    if(SUCCEEDED(hr))
        return hr;

    FIXME("%s: no class found.\n", debugstr_guid(rclsid));
    return CLASS_E_CLASSNOTAVAILABLE;
}

static HRESULT register_inf(BOOL doregister)
{
    HRESULT (WINAPI *pRegInstall)(HMODULE hm, LPCSTR pszSection, const STRTABLEA* pstTable);
    HMODULE hAdvpack;

    static const WCHAR wszAdvpack[] = {'a','d','v','p','a','c','k','.','d','l','l',0};

    hAdvpack = LoadLibraryW(wszAdvpack);
    pRegInstall = (void *)GetProcAddress(hAdvpack, "RegInstall");

    return pRegInstall(hProxyDll, doregister ? "RegisterDll" : "UnregisterDll", NULL);
}

/***********************************************************************
 *		DllRegisterServer (URLMON.@)
 */
HRESULT WINAPI DllRegisterServer(void)
{
    HRESULT hr;

    TRACE("\n");

    hr = URLMON_DllRegisterServer();
    return SUCCEEDED(hr) ? register_inf(TRUE) : hr;
}

/***********************************************************************
 *		DllUnregisterServer (URLMON.@)
 */
HRESULT WINAPI DllUnregisterServer(void)
{
    HRESULT hr;

    TRACE("\n");

    hr = URLMON_DllUnregisterServer();
    return SUCCEEDED(hr) ? register_inf(FALSE) : hr;
}

/***********************************************************************
 *		DllRegisterServerEx (URLMON.@)
 */
HRESULT WINAPI DllRegisterServerEx(void)
{
    FIXME("(void): stub\n");

    return E_FAIL;
}

/**************************************************************************
 *                 IsValidURL (URLMON.@)
 * 
 * Determines if a specified string is a valid URL.
 *
 * PARAMS
 *  pBC        [I] ignored, should be NULL.
 *  szURL      [I] string that represents the URL in question.
 *  dwReserved [I] reserved and must be zero.
 *
 * RETURNS
 *  Success: S_OK.
 *  Failure: S_FALSE.
 *  returns E_INVALIDARG if one or more of the args is invalid.
 *
 * TODO:
 *  test functionality against windows to see what a valid URL is.
 */
HRESULT WINAPI IsValidURL(LPBC pBC, LPCWSTR szURL, DWORD dwReserved)
{
    FIXME("(%p, %s, %d): stub\n", pBC, debugstr_w(szURL), dwReserved);

    if (dwReserved || !szURL)
        return E_INVALIDARG;

    return S_OK;
}

/**************************************************************************
 *                 FaultInIEFeature (URLMON.@)
 *
 *  Undocumented.  Appears to be used by native shdocvw.dll.
 */
HRESULT WINAPI FaultInIEFeature( HWND hwnd, uCLSSPEC * pClassSpec,
                                 QUERYCONTEXT *pQuery, DWORD flags )
{
    FIXME("%p %p %p %08x\n", hwnd, pClassSpec, pQuery, flags);
    return E_NOTIMPL;
}

/**************************************************************************
 *                 CoGetClassObjectFromURL (URLMON.@)
 */
HRESULT WINAPI CoGetClassObjectFromURL( REFCLSID rclsid, LPCWSTR szCodeURL, DWORD dwFileVersionMS,
                                        DWORD dwFileVersionLS, LPCWSTR szContentType,
                                        LPBINDCTX pBindCtx, DWORD dwClsContext, LPVOID pvReserved,
                                        REFIID riid, LPVOID *ppv )
{
    FIXME("(%s %s %d %d %s %p %d %p %s %p) Stub!\n", debugstr_guid(rclsid), debugstr_w(szCodeURL),
	dwFileVersionMS, dwFileVersionLS, debugstr_w(szContentType), pBindCtx, dwClsContext, pvReserved,
	debugstr_guid(riid), ppv);
    return E_NOINTERFACE;
}

/***********************************************************************
 *           ReleaseBindInfo (URLMON.@)
 *
 * Release the resources used by the specified BINDINFO structure.
 *
 * PARAMS
 *  pbindinfo [I] BINDINFO to release.
 *
 * RETURNS
 *  Nothing.
 */
void WINAPI ReleaseBindInfo(BINDINFO* pbindinfo)
{
    DWORD size;

    TRACE("(%p)\n", pbindinfo);

    if(!pbindinfo || !(size = pbindinfo->cbSize))
        return;

    CoTaskMemFree(pbindinfo->szExtraInfo);
    ReleaseStgMedium(&pbindinfo->stgmedData);

    if(offsetof(BINDINFO, szExtraInfo) < size)
        CoTaskMemFree(pbindinfo->szCustomVerb);

    if(pbindinfo->pUnk && offsetof(BINDINFO, pUnk) < size)
        IUnknown_Release(pbindinfo->pUnk);

    memset(pbindinfo, 0, size);
    pbindinfo->cbSize = size;
}

/***********************************************************************
 *           CopyStgMedium (URLMON.@)
 */
HRESULT WINAPI CopyStgMedium(const STGMEDIUM *src, STGMEDIUM *dst)
{
    TRACE("(%p %p)\n", src, dst);

    if(!src || !dst)
        return E_POINTER;

    *dst = *src;

    switch(dst->tymed) {
    case TYMED_NULL:
        break;
    case TYMED_FILE:
        if(src->u.lpszFileName && !src->pUnkForRelease) {
            DWORD size = (strlenW(src->u.lpszFileName)+1)*sizeof(WCHAR);
            dst->u.lpszFileName = CoTaskMemAlloc(size);
            if(!dst->u.lpszFileName)
                return E_OUTOFMEMORY;
            memcpy(dst->u.lpszFileName, src->u.lpszFileName, size);
        }
        break;
    case TYMED_ISTREAM:
        if(dst->u.pstm)
            IStream_AddRef(dst->u.pstm);
        break;
    case TYMED_ISTORAGE:
        if(dst->u.pstg)
            IStorage_AddRef(dst->u.pstg);
        break;
    case TYMED_HGLOBAL:
        if(dst->u.hGlobal) {
            SIZE_T size = GlobalSize(src->u.hGlobal);
            char *src_ptr, *dst_ptr;

            dst->u.hGlobal = GlobalAlloc(GMEM_FIXED, size);
            if(!dst->u.hGlobal)
                return E_OUTOFMEMORY;
            dst_ptr = GlobalLock(dst->u.hGlobal);
            src_ptr = GlobalLock(src->u.hGlobal);
            memcpy(dst_ptr, src_ptr, size);
            GlobalUnlock(src_ptr);
            GlobalUnlock(dst_ptr);
        }
        break;
    default:
        FIXME("Unimplemented tymed %d\n", src->tymed);
    }

    if(dst->pUnkForRelease)
        IUnknown_AddRef(dst->pUnkForRelease);

    return S_OK;
}

/***********************************************************************
 *           CopyBindInfo (URLMON.@)
 */
HRESULT WINAPI CopyBindInfo(const BINDINFO *pcbiSrc, BINDINFO *pcbiDest)
{
    DWORD size;
    HRESULT hres;

    TRACE("(%p %p)\n", pcbiSrc, pcbiDest);

    if(!pcbiSrc || !pcbiDest)
        return E_POINTER;
    if(!pcbiSrc->cbSize || !pcbiDest->cbSize)
        return E_INVALIDARG;

    size = pcbiDest->cbSize;
    if(size > pcbiSrc->cbSize) {
        memcpy(pcbiDest, pcbiSrc, pcbiSrc->cbSize);
        memset((char*)pcbiDest+pcbiSrc->cbSize, 0, size-pcbiSrc->cbSize);
    } else {
        memcpy(pcbiDest, pcbiSrc, size);
    }
    pcbiDest->cbSize = size;

    size = FIELD_OFFSET(BINDINFO, szExtraInfo)+sizeof(void*);
    if(pcbiSrc->cbSize>=size && pcbiDest->cbSize>=size && pcbiSrc->szExtraInfo) {
        size = (strlenW(pcbiSrc->szExtraInfo)+1)*sizeof(WCHAR);
        pcbiDest->szExtraInfo = CoTaskMemAlloc(size);
        if(!pcbiDest->szExtraInfo)
            return E_OUTOFMEMORY;
        memcpy(pcbiDest->szExtraInfo, pcbiSrc->szExtraInfo, size);
    }

    size = FIELD_OFFSET(BINDINFO, stgmedData)+sizeof(STGMEDIUM);
    if(pcbiSrc->cbSize>=size && pcbiDest->cbSize>=size) {
        hres = CopyStgMedium(&pcbiSrc->stgmedData, &pcbiDest->stgmedData);
        if(FAILED(hres)) {
            CoTaskMemFree(pcbiDest->szExtraInfo);
            return hres;
        }
    }

    size = FIELD_OFFSET(BINDINFO, szCustomVerb)+sizeof(void*);
    if(pcbiSrc->cbSize>=size && pcbiDest->cbSize>=size && pcbiSrc->szCustomVerb) {
        size = (strlenW(pcbiSrc->szCustomVerb)+1)*sizeof(WCHAR);
        pcbiDest->szCustomVerb = CoTaskMemAlloc(size);
        if(!pcbiDest->szCustomVerb) {
            CoTaskMemFree(pcbiDest->szExtraInfo);
            ReleaseStgMedium(&pcbiDest->stgmedData);
            return E_OUTOFMEMORY;
        }
        memcpy(pcbiDest->szCustomVerb, pcbiSrc->szCustomVerb, size);
    }

    size = FIELD_OFFSET(BINDINFO, securityAttributes)+sizeof(SECURITY_ATTRIBUTES);
    if(pcbiDest->cbSize >= size)
        memset(&pcbiDest->securityAttributes, 0, sizeof(SECURITY_ATTRIBUTES));

    if(pcbiSrc->pUnk)
        IUnknown_AddRef(pcbiDest->pUnk);

    return S_OK;
}

static BOOL text_richtext_filter(const BYTE *b, DWORD size)
{
    return size > 5 && !memcmp(b, "{\\rtf", 5);
}

static BOOL text_html_filter(const BYTE *b, DWORD size)
{
    if(size < 6)
        return FALSE;

    if((b[0] == '<'
                && (b[1] == 'h' || b[1] == 'H')
                && (b[2] == 't' || b[2] == 'T')
                && (b[3] == 'm' || b[3] == 'M')
                && (b[4] == 'l' || b[4] == 'L'))
            || (b[0] == '<'
                && (b[1] == 'h' || b[1] == 'H')
                && (b[2] == 'e' || b[2] == 'E')
                && (b[3] == 'a' || b[3] == 'A')
                && (b[4] == 'd' || b[4] == 'D'))) return TRUE;

    return FALSE;
}

static BOOL text_xml_filter(const BYTE *b, DWORD size)
{
    if(size < 7)
        return FALSE;

    if(b[0] == '<' && b[1] == '?'
            && (b[2] == 'x' || b[2] == 'X')
            && (b[3] == 'm' || b[3] == 'M')
            && (b[4] == 'l' || b[4] == 'L')
            && b[5] == ' ') return TRUE;

    return FALSE;
}

static BOOL audio_basic_filter(const BYTE *b, DWORD size)
{
    return size > 4
        && b[0] == '.' && b[1] == 's' && b[2] == 'n' && b[3] == 'd';
}

static BOOL audio_wav_filter(const BYTE *b, DWORD size)
{
    return size > 12
        && b[0] == 'R' && b[1] == 'I' && b[2] == 'F' && b[3] == 'F'
        && b[8] == 'W' && b[9] == 'A' && b[10] == 'V' && b[11] == 'E';
}

static BOOL image_gif_filter(const BYTE *b, DWORD size)
{
    return size >= 6
        && (b[0] == 'G' || b[0] == 'g')
        && (b[1] == 'I' || b[1] == 'i')
        && (b[2] == 'F' || b[2] == 'f')
        &&  b[3] == '8'
        && (b[4] == '7' || b[4] == '9')
        && (b[5] == 'A' || b[5] == 'a');
}

static BOOL image_pjpeg_filter(const BYTE *b, DWORD size)
{
    return size > 2 && b[0] == 0xff && b[1] == 0xd8;
}

static BOOL image_tiff_filter(const BYTE *b, DWORD size)
{
    static const BYTE magic1[] = {0x4d,0x4d,0x00,0x2a};
    static const BYTE magic2[] = {0x49,0x49,0x2a,0xff};

    return size >= 4 && (!memcmp(b, magic1, 4) || !memcmp(b, magic2, 4));
}

static BOOL image_xpng_filter(const BYTE *b, DWORD size)
{
    static const BYTE xpng_header[] = {0x89,'P','N','G',0x0d,0x0a,0x1a,0x0a};
    return size > sizeof(xpng_header) && !memcmp(b, xpng_header, sizeof(xpng_header));
}

static BOOL image_bmp_filter(const BYTE *b, DWORD size)
{
    return size >= 14
        && b[0] == 0x42 && b[1] == 0x4d
        && *(const DWORD *)(b+6) == 0;
}

static BOOL video_avi_filter(const BYTE *b, DWORD size)
{
    return size > 12
        && b[0] == 'R' && b[1] == 'I' && b[2] == 'F' && b[3] == 'F'
        && b[8] == 'A' && b[9] == 'V' && b[10] == 'I' && b[11] == 0x20;
}

static BOOL video_mpeg_filter(const BYTE *b, DWORD size)
{
    return size > 4
        && !b[0] && !b[1] && b[2] == 0x01
        && (b[3] == 0xb3 || b[3] == 0xba);
}

static BOOL application_postscript_filter(const BYTE *b, DWORD size)
{
    return size > 2 && b[0] == '%' && b[1] == '!';
}

static BOOL application_pdf_filter(const BYTE *b, DWORD size)
{
    return size > 4 && b[0] == 0x25 && b[1] == 0x50 && b[2] == 0x44 && b[3] == 0x46;
}

static BOOL application_xzip_filter(const BYTE *b, DWORD size)
{
    return size > 2 && b[0] == 0x50 && b[1] == 0x4b;
}

static BOOL application_xgzip_filter(const BYTE *b, DWORD size)
{
    return size > 2 && b[0] == 0x1f && b[1] == 0x8b;
}

static BOOL application_java_filter(const BYTE *b, DWORD size)
{
    return size > 4 && b[0] == 0xca && b[1] == 0xfe && b[2] == 0xba && b[3] == 0xbe;
}

static BOOL application_xmsdownload(const BYTE *b, DWORD size)
{
    return size > 2 && b[0] == 'M' && b[1] == 'Z';
}

static inline BOOL is_text_plain_char(BYTE b)
{
    if(b < 0x20 && b != '\n' && b != '\r' && b != '\t')
        return FALSE;
    return TRUE;
}

static BOOL text_plain_filter(const BYTE *b, DWORD size)
{
    const BYTE *ptr;

    for(ptr = b; ptr < b+size-1; ptr++) {
        if(!is_text_plain_char(*ptr))
            return FALSE;
    }

    return TRUE;
}

static BOOL application_octet_stream_filter(const BYTE *b, DWORD size)
{
    return TRUE;
}

static HRESULT find_mime_from_buffer(const BYTE *buf, DWORD size, const WCHAR *proposed_mime, WCHAR **ret_mime)
{
    LPCWSTR ret = NULL;
    int len, i, any_pos_mime = -1;

    static const WCHAR text_htmlW[] = {'t','e','x','t','/','h','t','m','l',0};
    static const WCHAR text_richtextW[] = {'t','e','x','t','/','r','i','c','h','t','e','x','t',0};
    static const WCHAR text_xmlW[] = {'t','e','x','t','/','x','m','l',0};
    static const WCHAR audio_basicW[] = {'a','u','d','i','o','/','b','a','s','i','c',0};
    static const WCHAR audio_wavW[] = {'a','u','d','i','o','/','w','a','v',0};
    static const WCHAR image_gifW[] = {'i','m','a','g','e','/','g','i','f',0};
    static const WCHAR image_pjpegW[] = {'i','m','a','g','e','/','p','j','p','e','g',0};
    static const WCHAR image_tiffW[] = {'i','m','a','g','e','/','t','i','f','f',0};
    static const WCHAR image_xpngW[] = {'i','m','a','g','e','/','x','-','p','n','g',0};
    static const WCHAR image_bmpW[] = {'i','m','a','g','e','/','b','m','p',0};
    static const WCHAR video_aviW[] = {'v','i','d','e','o','/','a','v','i',0};
    static const WCHAR video_mpegW[] = {'v','i','d','e','o','/','m','p','e','g',0};
    static const WCHAR app_postscriptW[] =
        {'a','p','p','l','i','c','a','t','i','o','n','/','p','o','s','t','s','c','r','i','p','t',0};
    static const WCHAR app_pdfW[] = {'a','p','p','l','i','c','a','t','i','o','n','/','p','d','f',0};
    static const WCHAR app_xzipW[] = {'a','p','p','l','i','c','a','t','i','o','n','/',
        'x','-','z','i','p','-','c','o','m','p','r','e','s','s','e','d',0};
    static const WCHAR app_xgzipW[] = {'a','p','p','l','i','c','a','t','i','o','n','/',
        'x','-','g','z','i','p','-','c','o','m','p','r','e','s','s','e','d',0};
    static const WCHAR app_javaW[] = {'a','p','p','l','i','c','a','t','i','o','n','/',
        'j','a','v','a',0};
    static const WCHAR app_xmsdownloadW[] = {'a','p','p','l','i','c','a','t','i','o','n','/',
        'x','-','m','s','d','o','w','n','l','o','a','d',0};
    static const WCHAR text_plainW[] = {'t','e','x','t','/','p','l','a','i','n','\0'};
    static const WCHAR app_octetstreamW[] = {'a','p','p','l','i','c','a','t','i','o','n','/',
        'o','c','t','e','t','-','s','t','r','e','a','m','\0'};

    static const struct {
        LPCWSTR mime;
        BOOL (*filter)(const BYTE *,DWORD);
    } mime_filters_any_pos[] = {
        {text_htmlW,       text_html_filter},
        {text_xmlW,        text_xml_filter}
    }, mime_filters[] = {
        {text_richtextW,   text_richtext_filter},
     /* {audio_xaiffW,     audio_xaiff_filter}, */
        {audio_basicW,     audio_basic_filter},
        {audio_wavW,       audio_wav_filter},
        {image_gifW,       image_gif_filter},
        {image_pjpegW,     image_pjpeg_filter},
        {image_tiffW,      image_tiff_filter},
        {image_xpngW,      image_xpng_filter},
     /* {image_xbitmapW,   image_xbitmap_filter}, */
        {image_bmpW,       image_bmp_filter},
     /* {image_xjgW,       image_xjg_filter}, */
     /* {image_xemfW,      image_xemf_filter}, */
     /* {image_xwmfW,      image_xwmf_filter}, */
        {video_aviW,       video_avi_filter},
        {video_mpegW,      video_mpeg_filter},
        {app_postscriptW,  application_postscript_filter},
     /* {app_base64W,      application_base64_filter}, */
     /* {app_macbinhex40W, application_macbinhex40_filter}, */
        {app_pdfW,         application_pdf_filter},
     /* {app_zcompressedW, application_xcompressed_filter}, */
        {app_xzipW,        application_xzip_filter},
        {app_xgzipW,       application_xgzip_filter},
        {app_javaW,        application_java_filter},
        {app_xmsdownloadW, application_xmsdownload},
        {text_plainW,      text_plain_filter},
        {app_octetstreamW, application_octet_stream_filter}
    };

    if(!buf || !size) {
        if(!proposed_mime)
            return E_FAIL;

        len = strlenW(proposed_mime)+1;
        *ret_mime = CoTaskMemAlloc(len*sizeof(WCHAR));
        if(!*ret_mime)
            return E_OUTOFMEMORY;

        memcpy(*ret_mime, proposed_mime, len*sizeof(WCHAR));
        return S_OK;
    }

    if(proposed_mime && (!strcmpW(proposed_mime, app_octetstreamW)
                || !strcmpW(proposed_mime, text_plainW)))
        proposed_mime = NULL;

    if(proposed_mime) {
        ret = proposed_mime;

        for(i=0; i < sizeof(mime_filters_any_pos)/sizeof(*mime_filters_any_pos); i++) {
            if(!strcmpW(proposed_mime, mime_filters_any_pos[i].mime)) {
                any_pos_mime = i;
                for(len=size; len>0; len--) {
                    if(mime_filters_any_pos[i].filter(buf+size-len, len))
                        break;
                }
                if(!len)
                    ret = NULL;
                break;
            }
        }

        if(i == sizeof(mime_filters_any_pos)/sizeof(*mime_filters_any_pos)) {
            for(i=0; i < sizeof(mime_filters)/sizeof(*mime_filters); i++) {
                if(!strcmpW(proposed_mime, mime_filters[i].mime)) {
                    if(!mime_filters[i].filter(buf, size))
                        ret = NULL;
                    break;
                }
            }
        }
    }

    /* Looks like a bug in native implementation, html and xml mimes
     * are not looked for if none of them was proposed */
    if(!proposed_mime || any_pos_mime!=-1) {
        for(len=size; !ret && len>0; len--) {
            for(i=0; i<sizeof(mime_filters_any_pos)/sizeof(*mime_filters_any_pos); i++) {
                if(mime_filters_any_pos[i].filter(buf+size-len, len)) {
                    ret = mime_filters_any_pos[i].mime;
                    break;
                }
            }
        }
    }

    i=0;
    while(!ret) {
        if(mime_filters[i].filter(buf, size))
            ret = mime_filters[i].mime;
        i++;
    }

    if(any_pos_mime!=-1 && ret==text_plainW)
        ret = mime_filters_any_pos[any_pos_mime].mime;
    else if(proposed_mime && ret==app_octetstreamW) {
        for(len=size; ret==app_octetstreamW && len>0; len--) {
            if(!is_text_plain_char(buf[size-len]))
                break;
            for(i=0; i<sizeof(mime_filters_any_pos)/sizeof(*mime_filters_any_pos); i++) {
                if(mime_filters_any_pos[i].filter(buf+size-len, len)) {
                    ret = text_plainW;
                    break;
                }
            }
        }

        if(ret == app_octetstreamW)
            ret = proposed_mime;
    }
    TRACE("found %s for %s\n", debugstr_w(ret), debugstr_an((const char*)buf, min(32, size)));

    len = strlenW(ret)+1;
    *ret_mime = CoTaskMemAlloc(len*sizeof(WCHAR));
    if(!*ret_mime)
        return E_OUTOFMEMORY;

    memcpy(*ret_mime, ret, len*sizeof(WCHAR));
    return S_OK;
}

/***********************************************************************
 *           FindMimeFromData (URLMON.@)
 *
 * Determines the Multipurpose Internet Mail Extensions (MIME) type from the data provided.
 */
HRESULT WINAPI FindMimeFromData(LPBC pBC, LPCWSTR pwzUrl, LPVOID pBuffer,
        DWORD cbSize, LPCWSTR pwzMimeProposed, DWORD dwMimeFlags,
        LPWSTR* ppwzMimeOut, DWORD dwReserved)
{
    TRACE("(%p,%s,%p,%d,%s,0x%x,%p,0x%x)\n", pBC, debugstr_w(pwzUrl), pBuffer, cbSize,
            debugstr_w(pwzMimeProposed), dwMimeFlags, ppwzMimeOut, dwReserved);

    if(dwMimeFlags)
        WARN("dwMimeFlags=%08x\n", dwMimeFlags);
    if(dwReserved)
        WARN("dwReserved=%d\n", dwReserved);

    /* pBC seams to not be used */

    if(!ppwzMimeOut || (!pwzUrl && !pBuffer))
        return E_INVALIDARG;

    if(pwzMimeProposed || pBuffer)
        return find_mime_from_buffer(pBuffer, cbSize, pwzMimeProposed, ppwzMimeOut);

    if(pwzUrl) {
        HKEY hkey;
        DWORD res, size;
        LPCWSTR ptr;
        WCHAR mime[64];

        static const WCHAR wszContentType[] =
                {'C','o','n','t','e','n','t',' ','T','y','p','e','\0'};

        ptr = strrchrW(pwzUrl, '.');
        if(!ptr)
            return E_FAIL;

        res = RegOpenKeyW(HKEY_CLASSES_ROOT, ptr, &hkey);
        if(res != ERROR_SUCCESS)
            return HRESULT_FROM_WIN32(res);

        size = sizeof(mime);
        res = RegQueryValueExW(hkey, wszContentType, NULL, NULL, (LPBYTE)mime, &size);
        RegCloseKey(hkey);
        if(res != ERROR_SUCCESS)
            return HRESULT_FROM_WIN32(res);

        *ppwzMimeOut = CoTaskMemAlloc(size);
        memcpy(*ppwzMimeOut, mime, size);
        return S_OK;
    }

    return E_FAIL;
}

/***********************************************************************
 *           GetClassFileOrMime (URLMON.@)
 *
 * Determines the class ID from the bind context, file name or MIME type.
 */
HRESULT WINAPI GetClassFileOrMime(LPBC pBC, LPCWSTR pszFilename,
        LPVOID pBuffer, DWORD cbBuffer, LPCWSTR pszMimeType, DWORD dwReserved,
        CLSID *pclsid)
{
    FIXME("(%p, %s, %p, %d, %s, 0x%08x, %p): stub\n", pBC, debugstr_w(pszFilename), pBuffer,
            cbBuffer, debugstr_w(pszMimeType), dwReserved, pclsid);
    return E_NOTIMPL;
}

/***********************************************************************
 * Extract (URLMON.@)
 */
HRESULT WINAPI Extract(void *dest, LPCSTR szCabName)
{
    HRESULT (WINAPI *pExtract)(void *, LPCSTR);

    if (!hCabinet)
        hCabinet = LoadLibraryA("cabinet.dll");

    if (!hCabinet) return HRESULT_FROM_WIN32(GetLastError());
    pExtract = (void *)GetProcAddress(hCabinet, "Extract");
    if (!pExtract) return HRESULT_FROM_WIN32(GetLastError());

    return pExtract(dest, szCabName);
}

/***********************************************************************
 *           IsLoggingEnabledA (URLMON.@)
 */
BOOL WINAPI IsLoggingEnabledA(LPCSTR url)
{
    FIXME("(%s)\n", debugstr_a(url));
    return FALSE;
}

/***********************************************************************
 *           IsLoggingEnabledW (URLMON.@)
 */
BOOL WINAPI IsLoggingEnabledW(LPCWSTR url)
{
    FIXME("(%s)\n", debugstr_w(url));
    return FALSE;
}

/***********************************************************************
 *           IsProtectedModeURL (URLMON.111)
 *    Undocumented, added in IE7
 */
BOOL WINAPI IsProtectedModeURL(const WCHAR *url)
{
    FIXME("stub: %s\n", debugstr_w(url));
    return TRUE;
}

/***********************************************************************
 *           LogSqmBits (URLMON.410)
 *    Undocumented, added in IE8
 */
int WINAPI LogSqmBits(DWORD unk1, DWORD unk2)
{
    FIXME("stub: %d %d\n", unk1, unk2);
    return 0;
}

/***********************************************************************
 *           LogSqmUXCommandOffsetInternal (URLMON.423)
 *    Undocumented, added in IE8
 */
void WINAPI LogSqmUXCommandOffsetInternal(DWORD unk1, DWORD unk2, DWORD unk3, DWORD unk4)
{
    FIXME("stub: %d %d %d %d\n", unk1, unk2, unk3, unk4);
}

/***********************************************************************
 *           MapUriToBrowserEmulationState (URLMON.444)
 *    Undocumented, added in IE8
 */
int WINAPI MapUriToBrowserEmulationState(DWORD unk1, DWORD unk2, DWORD unk3)
{
    FIXME("stub: %d %d %d\n", unk1, unk2, unk3);
    return 0;
}

/***********************************************************************
 *           MapBrowserEmulationModeToUserAgent (URLMON.445)
 *    Undocumented, added in IE8
 */
int WINAPI MapBrowserEmulationModeToUserAgent(DWORD unk1, DWORD unk2)
{
    FIXME("stub: %d %d\n", unk1, unk2);
    return 0;
}

/***********************************************************************
 *           FlushUrlmonZonesCache (URLMON.455)
 *    Undocumented, added in IE8
 */
void WINAPI FlushUrlmonZonesCache(void)
{
    FIXME("stub\n");
}

/***********************************************************************
 *            RegisterMediaTypes
 *    Added in IE3, registers known MIME-type strings.
 */
HRESULT WINAPI RegisterMediaTypes(UINT types, LPCSTR *szTypes, CLIPFORMAT *cfTypes)
{
   FIXME("stub: %u %p %p\n", types, szTypes, cfTypes);
   return E_INVALIDARG;
}
