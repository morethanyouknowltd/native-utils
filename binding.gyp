{
  "targets": [
    {
      "target_name": "nativeutils",
      "sources": [
        "src/native/main.cc",
      ],
      "include_dirs": [
        "<!(node -p \"require('node-addon-api').include_dir\")",
        "<!(node -p \"require('node-addon-api-helper').include_dir\")"
      ],
      'target_defaults': {
        'configurations': {
          'Debug': {
            'defines': [ 'DEBUG' ],
          },
        },
      },
      'cflags_cc!': [
        '-fno-exceptions',
        '-Wno-unused-variable'
        '-std=c++17'
      ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.13',
        'OTHER_CFLAGS': [ "-std=c++17" ]
      },
      'msvs_settings': {
        'VCCLCompilerTool': {
          'ExceptionHandling': 1,
          'AdditionalOptions': [ '-std:c++latest' ]
        }
      },
      'conditions': [
      ['OS == "mac"', {
        'defines': ['IS_MACOS'],
        'cflags+': ['-fvisibility=hidden'],
        'xcode_settings': {
          'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
        },
        'include_dirs': [
          'System/Library/Frameworks/CoreFoundation.Framework/Headers',
          'System/Library/Frameworks/CoreGraphics.Framework/Headers',
          'System/Library/Frameworks/ApplicationServices.framework/Headers'
        ],
        'link_settings': {
          'libraries': [
            '-framework CoreFoundation',
            '-framework CoreGraphics',
            '-framework ApplicationServices'
          ]
        },

      }],
      ['OS=="win"', {
        'defines': [
          'IS_WINDOWS',
          'NOMINMAX',
          'WINVER=0x0500',
          '_WIN32_WINNT=0x0600'
        ],
        'msbuild_settings': {
          'ClCompile': {
              'LanguageStandard': 'stdcpp17'
          }
        },
        'libraries': [
          "psapi.lib"
        ]
      }]
    ]
    }
  ]
}
