import pandas as pd

intro = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Big Picture applicative</title>
</head>
<body>
    <h1 style="text-align: center;">Page HTML</h1>
       {table}

</body>
</html>
'''


def convert_csv():
    df = pd.read_csv('fr-esr-jury-expert-aap-fonds-national-pour-la-science-ouverte.csv',
                     sep=',',
                     engine='python',
                     encoding='utf-8')
    df.fillna('',inplace=True)
    df.replace('\r', '-', regex=True, inplace=True)
    df.replace('\n', '-', regex=True, inplace=True)
    with open('csv.html', 'w') as doc:
        doc.write((intro.format(table=df.to_html(classes='my-table',
                                                 justify='center'))))

    if __name__ == '__main__':
        convert_csv()