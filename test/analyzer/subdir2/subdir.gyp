# Copyright (c) 2014 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'foo',
      'type': 'static_library',
      'sources': [
        'subdir_source.c',
      ],
      'includes': [
        'subdir.includes.gypi',
      ],
    },
  ],
}
