import matplotlib.pyplot as plt
from flask import Flask , render_template , request , redirect , url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, CollegePlacements
app= Flask(__name__)


engine = create_engine('sqlite:///placementsData.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session=DBSession()



@app.route('/')
@app.route('/view')
def HelloWorld():
         global values
         values=[]
         session=DBSession()
         a= session.query(CollegePlacements).all()
         for i in a:
             values+=[i.year]
         return render_template('output.html',a=a)


@app.route('/')
@app.route('/pl',methods=['GET','POST'])
def newStudent():
    if request.method == 'POST':
        newS = CollegePlacements(
            name=request.form['name'],id=request.form['id'],year=request.form['year'],company=request.form['company'],salary=request.form['salary'],dept=request.form['dept'])
        session.add(newS)
        session.commit()
        return redirect(url_for('HelloWorld'))
    else:
        return render_template('new_Student.html')


@app.route('/')
@app.route('/grV')
def graphView():
      plt.title("Placements data distribution yearwise")
      plt.hist(values,bins=5)
      plt.xticks([2013,2014,2015,2016,2017])
      plt.xlabel('Year')
      plt.ylabel('No. of Students')
      plt.show()
      return redirect(url_for('HelloWorld'))




if __name__=='__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port =8080)