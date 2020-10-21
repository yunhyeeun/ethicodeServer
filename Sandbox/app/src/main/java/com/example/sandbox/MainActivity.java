package com.example.sandbox;

import android.os.AsyncTask;
import android.os.Bundle;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;
import android.view.View;

import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    private TextView itemName;
    private TextView companyName;
    private EditText editText;
    private Button button;
    private String jsonString;
    ArrayList<Item> itemArrayList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        itemName = (TextView) findViewById(R.id.itemname);
        companyName = (TextView) findViewById(R.id.companyname);
        editText = (EditText) findViewById(R.id.editText);
        button = (Button) findViewById(R.id.button);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final JsonParse jsonParse = new JsonParse();
                jsonParse.execute("http://193.122.105.82/query.php");
            }
        });

    }

    public class JsonParse extends AsyncTask<String, Void, String> {
        String TAG = "JsonParseTest";

        @Override
        protected String doInBackground(String... strings) {
            String url = strings[0];
            try {
                String selectData = "?barcode=" + editText.getText().toString();
                Log.d(TAG, selectData);
                url = url + selectData;
                URL serverURL = new URL(url);
                HttpURLConnection httpURLConnection = (HttpURLConnection) serverURL.openConnection();

                httpURLConnection.setReadTimeout(5000);
                httpURLConnection.setConnectTimeout(5000);
                httpURLConnection.connect();

                int responseStatusCode = httpURLConnection.getResponseCode();

                InputStream inputStream;
                if (responseStatusCode == HttpURLConnection.HTTP_OK) {
                    inputStream = httpURLConnection.getInputStream();
                } else {
                    inputStream = httpURLConnection.getErrorStream();
                }

                InputStreamReader inputStreamReader = new InputStreamReader(inputStream, "UTF-8");
                BufferedReader br = new BufferedReader(inputStreamReader);

                StringBuilder sb = new StringBuilder();
                String line;

                while ((line = br.readLine()) != null) {
                    sb.append(line);
                }

                br.close();
                Log.d(TAG, sb.toString().trim());

                return sb.toString().trim();
             } catch (Exception e) {
                Log.d(TAG, "InsertData: Error", e);
                String errorString = e.toString();
                return null;
            }
        }

        @Override
        protected void onPostExecute(String fromdoInBackgroundString) {
            super.onPostExecute(fromdoInBackgroundString);

            if (fromdoInBackgroundString == null) {
                itemName.setText("error");
                itemName.setText("error");
            } else {
                jsonString = fromdoInBackgroundString;
                itemArrayList = doParse();
                if (itemArrayList.size() == 0) {
                    itemName.setText("NO RESULT");
                    companyName.setText("NO RESULT");
                } else {
                    itemName.setText(itemArrayList.get(0).getItemname());
                    companyName.setText(itemArrayList.get(0).getCompanyname());

                }
            }
        }

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }

        @Override
        protected void onProgressUpdate(Void... values) {
            super.onProgressUpdate(values);
        }

        @Override
        protected void onCancelled(String s) {
            super.onCancelled(s);
        }

        private ArrayList<Item> doParse() {
            ArrayList<Item> tmpItemArray = new ArrayList<>();
            try {
                JSONObject jsonObject = new JSONObject(jsonString);
                JSONArray jsonArray = jsonObject.getJSONArray("Item");

                for (int i = 0;i < jsonArray.length();i++) {
                    Item tmpItem = new Item();
                    JSONObject item = jsonArray.getJSONObject(i);
                    tmpItem.setBarcode(item.getString("BARCODE"));
                    tmpItem.setItemname(item.getString("ITEMNAME"));
                    tmpItem.setCompanyname(item.getString("COMPANYNAME"));
                    tmpItemArray.add(tmpItem);
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }

            return tmpItemArray;
        }
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}