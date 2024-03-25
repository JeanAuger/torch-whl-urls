# Torch dependency
CLI util to get the full wheel URLs of torch dependencies

## Usage
Print the relevant URLs from the following commands' `stdout`:

    python -m src torch -v 2.2.0
    python -m src torch -v 2.2.0 --device cuda
    
    python -m src torchvision -v 2.2.0
    python -m src torchvision -v 2.2.0 --device cuda

