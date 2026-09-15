# Merge Conflict Resolution

## What happened
Two feature branches were created from `develop` in parallel:

- `feature/version-endpoint` added a module-level constant
  `APP_VERSION = "1.0.0"` on the line immediately after
  `app = Flask(__name__)`.
- `feature/environment-endpoint` added a different module-level constant
  `APP_ENV = os.environ.get("APP_ENVIRONMENT", "development")` on that
  same line.

`feature/version-endpoint` was merged into `develop` first, cleanly.
When `feature/environment-endpoint` was then merged into `develop`, Git
could not automatically reconcile the two branches because both had
edited the same location in `app.py` with different content.

## The conflict
Git paused the merge and marked the region in `app.py`:

    app = Flask(__name__)
    <<<<<<< HEAD
    APP_VERSION = "1.0.0"
    =======
    APP_ENV = os.environ.get("APP_ENVIRONMENT", "development")
    >>>>>>> feature/environment-endpoint

## How it was resolved
Both constants were genuinely needed, so the resolution was to keep
both lines and remove the conflict markers:

    app = Flask(__name__)
    APP_VERSION = "1.0.0"
    APP_ENV = os.environ.get("APP_ENVIRONMENT", "development")

The change was staged and the merge committed with:

    git add app.py
    git commit -m "merge: resolve conflict between version and environment constants"

The routes themselves (`/version` and `/environment`) sat further down
the file and merged without conflict.

## Lesson
The conflict arose because two branches modified the same line region.
Keeping edits in separate parts of a file, or coordinating shared
sections early, reduces this kind of collision.