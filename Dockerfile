FROM python:3.10.0-alpine
ENV PYTHONUNBUFFERED 1
# Set the working directory in the container
WORKDIR /gadgets
# Copy the project code to the container
COPY . /gadgets/
# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput
# Apply database migrations
RUN python manage.py migrate --noinput
# Load database data
RUN python manage.py loaddata gadgets.json