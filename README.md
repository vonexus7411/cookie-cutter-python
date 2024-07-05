# Cookiecutter Python

## Instructions
### Using cookiecutter CLI

1. Install cookiecutter with either Chocolatey or `pip install cookiecutter`.
2. Run `cookiecutter git@ssh.dev.azure.com:v3/ad-vestcom/Vestcom/cookiecutter-python`
3. Follow the prompts to set up your new Python environment.

```
$ cookiecutter git@ssh.dev.azure.com:v3/ad-vestcom/Vestcom/cookiecutter-python

  [1/6] project_name (My Python Application): 
  [2/6] project_slug (my_python_application):
  [3/6] author (Vestcom Data Engineering):
  [4/6] Select use_spark
    1 - yes
    2 - no
    Choose from [1/2] (1):
  [5/6] Select use_hadoop
    1 - yes
    2 - no
    Choose from [1/2] (1):
  [6/6] Select dev_mode
    1 - yes
    2 - no
    Choose from [1/2] (1):

$ code .\my_python_application\
```

### Using the sample

Either clone or fork `https://dev.azure.com/ad-vestcom/Vestcom/_git/cookiecutter-python.sample` and update as necessary.  Please view the README.md for instructions to safely guard your container before going to production.

## Notes

Author: Vestcom Data Engineering