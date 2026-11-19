// One Day — 18 November 2026: entrypoint written for this entry.
// The finished front page lives beside this file as entry.png; the grader
// expects those exact bytes at /output/entry.png, so this program performs
// one deterministic copy and exits. No network, no clock, no randomness:
// running it twice yields identical output.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoDir = dirname(fileURLToPath(import.meta.url));
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(targetDir, { recursive: true });
copyFileSync(join(repoDir, "entry.png"), join(targetDir, "entry.png"));
