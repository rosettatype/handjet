"""
A helper script that will cross-check Rosetta’s glyphsDB with all .nam files in
a folder and output a list of Rosetta names (and highlight glyphs missing from
glyphsDB)
"""
import pickle
import os
from glyphsdb.glyphsdb import GlyphsDB
from glyphsdb.util.parser import parse_glyphs_from_nam

# For convenience, save the DB locally so we don't need to recompile every run
db_file = "db.pkl"
if not os.path.isfile(db_file):
    print("Writing cached db file to %s" % db_file)
    db = GlyphsDB()
    db.load_folder()
    pickle.dump(db, open(db_file, "wb"))
else:
    print("Loading cached db file from %s" % db_file)
    db = pickle.load(open(db_file, "rb"))


# Parse the nam files
folder = os.path.join(os.path.split(os.path.abspath(__file__))[0], "nam")
glyphs = parse_glyphs_from_nam(folder)
print("Processing a total of %d glyphs from all .nam files in %s" %
      (len(glyphs), folder))

# Find Rosetta names
invalid = []
for i, r in enumerate(glyphs):
    rosetta_name = db.get_rosetta_name(unicode=r["unicode"],
                                       name=r["name"])
    if not rosetta_name:
        invalid.append(r)
        print("Missing rosetta name for", r)
    else:
        glyphs[i]["rosetta_name"] = rosetta_name

# Print missing glyphs to console or output the charset with all Rosetta names
if len(invalid) == 0:
    charset = "gf-charset-rosetta-names.txt"
    glyphlines = [g["rosetta_name"] for g in glyphs]
    # make unique
    glyphlines = list(set(glyphlines))

    with open(charset, "w") as file:
        file.writelines([g + "\n" for g in glyphlines])
    print("Written all %d unique glyphs as Rosetta glyphnames to %s" %
          (len(glyphlines), charset))
else:
    print("Add the above glyphs to the glyphsDB")
