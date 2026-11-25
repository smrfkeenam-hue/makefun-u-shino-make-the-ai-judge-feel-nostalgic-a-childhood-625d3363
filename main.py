import os

# One sentence (<=280 chars): a childhood memory, written to entry.txt
# with no trailing newline.
ENTRY = "On rainy afternoons I sat on Grandma's cold kitchen tiles stealing warm rice from the pot with my fingers while she pretended not to notice, the smell of fried shallots hanging in the air like it would never leave."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
