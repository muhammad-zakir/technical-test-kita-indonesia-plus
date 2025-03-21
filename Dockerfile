FROM python:3.12-slim AS builder

# Create the working directory
RUN mkdir /application
# Set the working directory
WORKDIR /application

# Set environment variables to optimize Python
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

# Upgrade pip
RUN pip install --upgrade pip 

# Copy the Django project  and install dependencies
COPY requirements.txt  /application/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS runner

RUN useradd -m -r applicationuser && \
  mkdir /application && \
  chown -R applicationuser /application

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /application

# Copy application code
COPY --chown=applicationuser:applicationuser . .

# Set environment variables to optimize Python
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

# Switch to non-root user
USER applicationuser

# Expose the application port
EXPOSE 8000 
 
# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "library.wsgi:application"]