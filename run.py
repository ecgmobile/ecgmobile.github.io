#!/usr/bin/env python

import os
from ecgmobile import main

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    main.app.run(host='0.0.0.0', port=port)