#!/usr/bin/perl
use strict;
use warnings;
use CGI;

# Crear un nuevo objeto CGI
my $query = CGI->new;

# Obtener el término de búsqueda pasado como argumento
my $search_term = $ARGV[0] || '';

# Imprimir la cabecera HTTP y el contenido HTML
print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html>
<html>
<head>
    <title>Resultados de Búsqueda</title>
</head>
<body>
    <h1>Resultados para: $search_term</h1>
    <!-- Aquí puedes añadir el código para mostrar los resultados de la búsqueda -->
</body>
</html>
HTML
