from flask import Flask, render_template, request, redirect,escape
from search import search

app = Flask(__name__)  # определяет текущее активное пространство имён __name__

if __name__ == '__main__':
    print(__name__)  # если мы запускаем непосредственно этот файл то выполниться это условие и __name__=__main__
else:
    print(__name__)  # если мы этот файл импортировали как модуль то __name__=web(соответствует имени модуля)


@app.route('/')
def hello() -> 302:  # code redirect
    return redirect('/entry')  # если мы введём / то сервер нас перенаправит на адрес /entry


@app.route('/find', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = search(phrase=phrase, letters=letters)

    file = open('data/results.txt', 'a')  # созда'м файловій дескриптор
    print('Our phrase,letters,result:', phrase, letters, result, file=file)  # записываем данные в файл
    file.close()  # не забыть закрыть файл

    log_request(request, result)

    return render_template('result.html',
                           the_title="Our Result",
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=result)


def log_request(req: 'flask_request', res: str) -> None:
    with open('data/search.log', 'a') as file:
        print(req.form, req.user_agent, req.remote_addr, res, file=file, sep='|')


@app.route('/viewlog')
def view_the_log() -> 'html':
    with open('data/search.log') as log:
        the_title = 'View_Log'
        contents = []
        row_titles = ['Form Data', 'Remote_addr', 'User_agent', 'Results']
        list = log.readlines()
        for row in list:
            contents.append(escape(row.split('|')))#escapе экранирует теги html если таковые есть

    return render_template('viewlog.html',
                           the_title=the_title,
                           row_titles=row_titles,
                           log=contents)


@app.route('/first_page')  # 1 вариант как попасть на странницу
@app.route('/entry')  # 2 вариант
def entry() -> 'html':
    # послает html форму с параметрами для вставки данных в неё пользователю
    return render_template('entry.html', the_title='Welcome to my first web project on python')


if __name__ == '__main__':  # если мы импортируем этот модуль то следующая строчка не отработает так как значение
    # __name__ будет web
    # это нужно чтобы при развёртывании приложения на PythonAnywhere наше приложение запускала эту  служба а не мы сами
    app.run(debug=True)  # debug=True означает что приложение будет обновляться автоматически без перезапуска сервера
    # вручную


