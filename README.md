# python_envs_backup

Python code for automatic creation of env files for every exising environment in an Anaconda installation.

The code create and mantains the following folder structure:

```
year_directory
  |
  +-- month1_directory
  |   |
  |   +-- day1_directory
  |   +-- day2_directory
  |   +-- day3_directory
  |
  |
  +-- month2_directory
      |
      +-- day1_directory
      +-- day2_directory
      +-- day3_directory
```

Every new day/month/year a new directory will be created, and directories older than 1 year will be deleted.
Can be scheduled on the os, and variables "envs_dir" and "backups_dir" should be changed to reflect the correct paths for the anaconda and backups directories, respectively.
