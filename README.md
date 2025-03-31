## Job-Hunt-AI
this repo is created by Team Avengers(AMAN, RAHUL, ABHINN, SONAL) for hackathon within Techpix Organisation

## Step to run

Build image
* docker build -t job-hunt-ai:latest --file deployments/Dockerfile .

Run Container
* docker run --name job-hunt-ai -p 8000:8000 -d job-hunt-ai:latest 
