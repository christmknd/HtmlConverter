import pandas as pd

intro = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Excel to HTML</title>
</head>
<body>
       <h1 style="text-align: center;">Recherche de mots clés</h1>

    <section>
        <div class="excel">
            {table}
        </div>
    </section>
</body>
</html>
'''

def excel_to_html():
    df = pd.read_excel('Recherche de mots clés.xlsx')
    df.fillna('', inplace=True)
    with open('recherche.html','w') as doc:
        doc.write(intro.format(table=df.to_html(classes='my-table',
                                                justify='center')))

if __name__ == '__main__':
    excel_to_html()