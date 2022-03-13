# Install Python with Nix

## Find packages and install

```bash
# list all python3 packages
nix-env -qa python3 --json
# pipe to jq
nix-env -qa python3 --json | jq '.[] |= .name'

# select a version, for example python39Full
nix-env -iA nixpkgs.python39Full

# reload shell
```

## Remove a previously install python

```bash
# query installed packages
nix-env -q

# remove python3 package
nix-env --uninstall python3
```
