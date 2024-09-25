<!-- montagem.php -->
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = htmlspecialchars($_POST['nome']);
    $email = htmlspecialchars($_POST['email']);
    $senha = htmlspecialchars($_POST['senha']);
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Montagem de Equipamento</title>
</head>
<body>
    <h2>Olá <?php echo $nome; ?>, você deseja obter informações de quais produtos?</h2>

    <form action="escolhas.php" method="POST">
        <input type="hidden" name="nome" value="<?php echo $nome; ?>">
        <button type="submit" name="produto" value="Notebook">Notebook</button>
        <button type="submit" name="produto" value="Desktop">Desktop</button>
    </form>
</body>
</html>