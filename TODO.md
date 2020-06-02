# TODO

## Design

- [ ] check Arabic marks and spacing
- [ ] document features (animals, symbols, patterns)

## Production:

- [x] review vertical metrics
- [ ] expand frac feature that currently works only for single digit arbitrary nut fractions (via kerning sup/inf against fraction-slash)
- [x] set up open-source production
- [ ] add licence and credits files

### Production backlog

- [ ] refactor automating the writing of the entire designspace on compile (e.g. adopt create-designspace-instances.py script to write out also axis mappings and sources) - the current designspace is based on a fontmake extracted designspace that was manually modified, but since the sources no longer contain those masters, there is no easy way to "recreate" that extracted designspace