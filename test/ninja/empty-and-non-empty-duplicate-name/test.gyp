# Copyright (c) 2014 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'All',
      'type': 'none',
      'dependencies': [
        'subdir/included.gyp:included_empty_target'
      ]
    },
    {
      'target_name': 'empty_target',
      'type': 'none',
    },
  ],
}
