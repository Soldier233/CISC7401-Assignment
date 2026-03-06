# User Instructions for this Project

## 1. Create a New Python Environment

Use the following command to create a new environment with Python 3.8:

```bash
conda create --name <env_name> python=3.8
```

Replace `<env_name>` with your desired environment name.

## 2. Activate the Environment

After creating the environment, activate it using the following command:

```bash
conda activate <env_name>
```

Replace `<env_name>` with the name of your environment.

## 3. Install Required Python Libraries

Once your environment is active, install the necessary libraries by running:

```bash
pip install -r requirements.txt
```

## 4. Complete the Code Segment

Fill in the code sections marked with `# Student Implementation:` in the provided scripts.

## 5. Run the Training Phase

Execute the following command to start the training process:

```bash
python main.py --train_ql --train_sa
```

## 6. Run the Testing Phase

After training, run the testing phase with:

```bash
python main.py --test_ql --test_sa
```

