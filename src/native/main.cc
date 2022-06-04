#include <napi.h>

#if defined(IS_MACOS)
#include <CoreFoundation/CoreFoundation.h>
#include <ApplicationServices/ApplicationServices.h>
#endif

#include "point.h"
#include "rect.h"
#include "window.h"
#include <iostream>

Napi::Object InitAll(Napi::Env env, Napi::Object exports)
{
  try
  {
    InitWindow(env, exports);
    return exports;
  }
  catch (const std::exception &e)
  {
    std::cerr << e.what() << std::endl;
  }
  catch (...)
  {
    std::cout << "OMG! an unexpected exception has been caught" << std::endl;
  }
  return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, InitAll)
