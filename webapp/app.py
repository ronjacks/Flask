from flask import Flask, render_template,url_for,send_file

app = Flask(__name__,static_url_path='/static')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/dallas/')
def dallas():
	img_file = url_for('static', filename='images/TimeofCrime.png')
	img_df_council= url_for('static', filename='images/df_council.jpg')
	img_df_division= url_for('static', filename='images/df_division.jpg')
	img_df_hourly= url_for('static', filename='images/df_hourly.jpg')
	img_df_month= url_for('static', filename='images/df_month.jpg')
	img_df_type_of_loc= url_for('static', filename='images/df_Type_of_Location.jpg')
	img_confusion_svm= url_for('static', filename='images/ConfusionmatrixSVMModel.png')
	img_confusion_XGB= url_for('static', filename='images/ConfusionmatrixGBoostModel.png')
	img_council_heatmap= url_for('static', filename='images/df_council_heatmap.png')

	return render_template("dallas.html",user_image = img_file,img_df_council=img_df_council,
	img_df_division=img_df_division,img_df_hourly=img_df_hourly,
	img_df_month=img_df_month,img_df_type_of_loc=img_df_type_of_loc,img_confusion_svm=img_confusion_svm,
	img_confusion_XGB=img_confusion_XGB,img_council_heatmap=img_council_heatmap)
	
	
@app.route('/about/')
def about():
	img_file = url_for('static', filename='images/TimeofCrime.png')
	img_df_council= url_for('static', filename='images/df_council.jpg')
	img_df_division= url_for('static', filename='images/df_division.jpg')
	img_df_hourly= url_for('static', filename='images/df_hourly.jpg')
	img_df_month= url_for('static', filename='images/df_month.jpg')
	img_df_type_of_loc= url_for('static', filename='images/df_Type_of_Location.jpg')
	img_confusion_svm= url_for('static', filename='images/ConfusionmatrixSVMModel.png')
	img_confusion_XGB= url_for('static', filename='images/ConfusionmatrixGBoostModel.png')
	img_council_heatmap= url_for('static', filename='images/df_council_heatmap.png')

	return render_template("about.html",user_image = img_file,img_df_council=img_df_council,
	img_df_division=img_df_division,img_df_hourly=img_df_hourly,
	img_df_month=img_df_month,img_df_type_of_loc=img_df_type_of_loc,img_confusion_svm=img_confusion_svm,
	img_confusion_XGB=img_confusion_XGB,img_council_heatmap=img_council_heatmap)
	
@app.route('/dallas_crime_choropleth/')
def dallas_crime_choropleth():
	return render_template('dallas_crime_choropleth.html')

@app.route('/dallas_severity1_crime_map/')
def dallas_severity1_crime_map():
	return render_template('dallas_severity1_crime_map.html')
	
@app.route('/dallas_severity2_crime_map/')
def dallas_severity2_crime_map():
	return render_template('dallas_severity2_crime_map.html')

@app.route('/dallas_severity3_crime_map/')
def dallas_severity3_crime_map():
	return render_template('dallas_severity3_crime_map.html')
	
if __name__ == '__main__':
    app.run(debug=True)
