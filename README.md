# Windows-Batch-Master
Initialize projects like a boss. Batch files to the rescue! 
Open power shell and run the command below. But make sure you're in the correct directory though.
I'm gonna have to do more research to make this repository an ideal one, this is just a starter.

```powershell

  PS E:\ <the_batch_file>.bat <PROJECT_NAME>

```
**Example:**
___

The `create_deep_learning_project.bat` creates the following project tree:

```powershell
project_root/
├───.git
├─── README.md
├─── requirements.txt
├───config
├───data
│   ├───external
│   ├───processed
│   └───raw
├───docs
├───experiments
├───models
│   └───pretrained_models
├───notebooks
│   ├───eda
│   ├───evaluation
│   └───model_development
├───outputs
│   └───predictions
├───results
│   ├───figures
│   ├───logs
│   └───model_weights
├───src
│   ├───data_preprocessing
│   ├───evaluate
│   ├───model
│   ├───train
│   └───utils
└───tests
    ├───integration_tests
    └───unit_tests
```

and there you go, you have a whole git repository initialized along with a template to a nicely organized project.
Now get to work!

___
