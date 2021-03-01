-------------installer postgres en local------------------
apt-get -y install postgresql
apt install postgresql postgresql-client
sudo service postgresql start
sudo -i -u postgres
psql

-------------docker postgres------------------------------
docker pull postgres
docker run --name -itd test_postgres -e POSTGRES_PASSWORD=test postgres
docker exec -it test_postgres bash
su postgres
psql