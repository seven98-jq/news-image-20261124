import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

// Copy this repository's entry.png to the output directory.
// The grader sets MAKEFUN_OUTPUT_DIR; without it, /output is used.
const outDir = resolve(process.env.MAKEFUN_OUTPUT_DIR || "/output");
const here = dirname(fileURLToPath(import.meta.url));
const dest = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), dest);
console.log(`wrote ${dest} (${statSync(dest).size} bytes)`);
