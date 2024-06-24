# Gunakan image Python sebagai base
FROM python:3.11-slim

# Atur direktori kerja di dalam container
WORKDIR /app

# Instal dependensi sistem yang diperlukan
# Instal dependensi sistem yang diperlukan
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    pkg-config \
    default-libmysqlclient-dev \
    && apt-get clean

# Perbarui pip
RUN pip install --upgrade pip

# Salin file requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependencies dari requirements.txt
RUN pip install  -r requirements.txt

# Salin seluruh kode aplikasi ke dalam container
COPY . /app/

# Atur variabel lingkungan untuk Django
ENV DJANGO_SETTINGS_MODULE=mysite.settings
ENV PYTHONUNBUFFERED=1

# Buat dan migrasi database (opsional, bisa dilakukan di luar container juga)
RUN python manage.py migrate

# Expose port yang digunakan oleh Django (misalnya 8000)
EXPOSE 8000

# Jalankan server Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
