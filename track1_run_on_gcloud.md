To deploy your Track 1 project directly from your local VS Code terminal, you will first need to install the Google Cloud CLI (`gcloud`) and then execute the deployment commands to package your agent and push it to Cloud Run.

Here is the step-by-step guide to deploying your agent locally:

### 1. Install and Authenticate the Google Cloud CLI
First, download and install the Google Cloud CLI for Windows from the official Google Cloud website. Once installed, **restart VS Code completely** so your terminal recognizes the `gcloud` command. 

Then, open your VS Code terminal and authenticate your Google account by running:
```bash
gcloud auth login
gcloud auth application-default login
```

### 2. Set Your Project ID
Set your active Google Cloud project so the CLI knows where to deploy the resources. Replace `your-project-id` with your actual Project ID:
```bash
gcloud config set project your-project-id
```

### 3. Enable Required Google Cloud APIs
To use Cloud Run, Artifact Registry, and Cloud Build, you must enable their respective APIs in your Google Cloud project. Run the following command in your terminal:
```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com aiplatform.googleapis.com compute.googleapis.com
```
When this finishes, you should see a message indicating the operation finished successfully.

### 4. Create and Configure a Service Account
You need to create a dedicated service account for your Cloud Run service so it operates with specific permissions rather than broad default access. Run this command to create the account:
```bash
gcloud iam service-accounts create research-agent-svc --display-name="Service Account for Track 1"
```
Next, grant this new service account the "Vertex AI User" role, which gives it permission to call Google's Gemini models in the cloud:
```bash
gcloud projects add-iam-policy-binding <your-project-id> --member="serviceAccount:research-agent-svc@<your-project-id>.iam.gserviceaccount.com" --role="roles/aiplatform.user"
```

### 5. Deploy the Agent to Cloud Run
Now it is time to deploy! We will use the `adk deploy cloud_run` command, which automates packaging your code into a Docker container, pushing it to the Artifact Registry, and launching the serverless service. 

Run the following command in your terminal (make sure you are in the root directory of your project where your `adk_agent` folder and `.env` file live):
```bash
adk deploy cloud_run --project=<your-project-id> --region=us-central1 --service_name=autonomous-research-agent --with_ui . -- --labels=dev-tutorial=codelab-adk --service-account=research-agent-svc@<your-project-id>.iam.gserviceaccount.com
```
*(Note: You can change the `--region` if you prefer a different Google Cloud region like `europe-west1` or `asia-south1`)*.

**During the deployment, you may be prompted with two questions:**
1.  If prompted to create an Artifact Registry Docker repository to store built containers, type **`Y`** and press ENTER.
2.  If prompted to allow unauthenticated invocations to your service name, type **`y`** and press ENTER. **This is important because it allows you to access the web UI without setting up a complex authentication firewall just for testing**.

### 6. Test Your Live Application
This deployment command will take a few minutes to finish running. Upon successful execution, the terminal will provide a public URL of your deployed Cloud Run service (it will look something like `https://autonomous-research-agent-123456.us-central1.run.app`). 

Open that URL in your browser, toggle on "Token Streaming" in the upper right, and test your agent! 

