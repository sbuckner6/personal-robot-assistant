# Personal Robot Assistant

A silly little Flask app that will answer your questions. Makes use of the Houndify API for knowledge gathering and Redis for local caching. Future versions will include SMS communication with the app via Sinch, speech recognition and synthesis, and possibly vision, and will most likely be tested on my Raspberry Pi 3.

## Getting Started

Make sure you have Docker and Docker-Compose installed and run the following in the root directory:

```
docker-compose --project-name personal-robot-assistant -f docker-compose.yml up
```