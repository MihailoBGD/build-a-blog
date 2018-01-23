from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lozinka@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    #next 3 lines are the db columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.String(600))

    def __init__(self, title, text):
        self.title = title
        self.text = text 

@app.route('/')
def index():

    blogs = Blog.query.all()
    '''
    blogs = [blogObj1, blogObj2, blogObj3]
    '''
    return render_template('blog-main.html',
                            title="Build-a-blog",
                            blogs = blogs)

@app.route('/new-blog-entry', methods=['POST', 'GET'])
def new_blog_entry():
    if request.method == 'POST':
        title_error = ""
        text_error = ""

        '''
        request.form = {
        "title": "abc",
        "text" : "abcdef"
        }
        '''
        blog_title = request.form['title']
        blog_text = request.form['text']
        if not blog_title:
            title_error = "title field requires text sir"
        if not blog_text:
            text_error = "text field requires text sir"
        if title_error or text_error:
            return render_template('new-blog-entry.html',
                                    title_error = title_error, 
                                    text_error = text_error)


        blog = Blog(blog_title, blog_text)
        db.session.add(blog)
        db.session.commit()
        return redirect("/")

    return render_template('new-blog-entry.html',title="Add-a-blog")


'''
@app.route('/blog-main', methods=['POST', 'GET'])
def blog-main():
    

@app.route('/single-blog', methods=['POST', 'GET'])
def single-blog():
'''    


@app.route('/delete-task', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()

'''
    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Blog(task_name)
        db.session.add(new_task)
        db.session.commit()
'''    