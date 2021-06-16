
template = """name: workflow-chain-%i

on:

  workflow_dispatch:
    branches: [main]

  workflow_run:
    workflows: [workflow-chain-%i]
    branches: [main]
    types:
      - completed

jobs:

  workflow-chain-%i:
    runs-on: Ubuntu-20.04
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    steps:

    - name: workflow-chain-%i
      run:  echo workflow-chain-%i
"""


for i in range(1,10):

    print (template%(i, i-1, i, i, i) )
    
    with open("./.github/.workflows/workflow-chain-%i.yml"%i, 'w') as f:
        f.write(template%(i, i-1, i, i, i))
