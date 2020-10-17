![Build Status](https://raw.githubusercontent.com/C0MODIN/radios-argentinas/main/imagenes/separador.png)]

# Recolección de radios Argentinas
Pequeño script en python que recolecta radios y los agrega en un archivo M3u.

  - Las radios se extrajeron de (https://gist.github.com/pisculichi/fae88a2f5570ab22da53).
  - Se incluyen radios extraidas de comentarios.
  - Ultima comentario extraido >>> 15/10/2020

# Como sumar tu radio en los comentarios
Dejar en los comentarios la radio que desea publicar de la siguiente manera: 
  - {AM o FM} [Nombre radio] (URL)

# Como se arma la lista

Se agregan las radios en un archivo "radios.txt" donde debe respetarse el formato que se expuso anteriormente.
{FM} [Nombre de tu radio 1] (Tu URL1)
{AM} [Nombre de tu radio 2] (Tu URL2)

Se ejecuta el archivo python, el cual arma la lista final.

```sh
$ python3 recolector_radios_m3u.py
```
Archivo final
>>> final_list.m3u

### Filtrar radios activas
[iptv-checker]: <https://www.npmjs.com/package/iptv-checker>
[iptv-check]: <https://github.com/peterpt/IPTV-CHECK>
Para limpiar la lista de radios que no se encuentren activas hacemos uso de dos herramientas.
  * [iptv-checker] - Node.js CLI tool for checking links in IPTV playlists.
  * [iptv-checker] - Script tool to validate url's online.
