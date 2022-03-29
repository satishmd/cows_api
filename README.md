# COWS API
---------------

## Installation & Deployment Guide

### 1. pull the project from the git hub repo
    git clone ---

### 2. build the application
    docker-compose -f docker-compose.yml build

### 3. start the application
    docker-compose -f docker-compose.yml up

### 4. running migrations
    docker-compose run web python manage.py migrate
