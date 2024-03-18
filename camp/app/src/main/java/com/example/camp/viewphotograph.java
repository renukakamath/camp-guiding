package com.example.camp;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class viewphotograph extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {

    ListView l1;
    SharedPreferences sh;
    String[] photographer_id,fname,lname,place,value,phone,email,login_id;
    public static String pid,lid,stat;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewphotograph);

        l1=(ListView) findViewById(R.id.list);
        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) viewphotograph.this;
        String q = "/viewphotograph?log_id=" +sh.getString("login_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {
        try {

            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                JSONArray ja1 = (JSONArray) jo.getJSONArray("data");

                fname = new String[ja1.length()];
                lname = new String[ja1.length()];
                place = new String[ja1.length()];
                phone = new String[ja1.length()];

                email = new String[ja1.length()];
                login_id = new String[ja1.length()];

                photographer_id = new String[ja1.length()];
                value = new String[ja1.length()];


                for (int i = 0; i < ja1.length(); i++) {
                    login_id[i] = ja1.getJSONObject(i).getString("login_id");

                    photographer_id[i] = ja1.getJSONObject(i).getString("photographer_id");

                    fname[i] = ja1.getJSONObject(i).getString("fname");
                    lname[i] = ja1.getJSONObject(i).getString("lname");
                    place[i] = ja1.getJSONObject(i).getString("place");

                    phone[i] = ja1.getJSONObject(i).getString("phone");
                    email[i] = ja1.getJSONObject(i).getString("email");




                    value[i] = "fname:" + fname[i] + "\n lname: " + lname[i] + "\n place: " + place[i]  + "\n phone: " + phone[i] + "\n email: " + email[i]  ;

                }
                ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), R.layout.custtext, value);

                l1.setAdapter(ar);



            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), "no photograph", Toast.LENGTH_LONG).show();

        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        pid=photographer_id[i];
        lid=login_id[i];

        final CharSequence[] items = {"booknow","Chat","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(viewphotograph.this);
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {
                if (items[item].equals("booknow")) {



                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) viewphotograph.this;
                    String q = "/booknow?log_id=" +sh.getString("login_id", "")+"&pid="+pid;
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }

                else if (items[item].equals("Chat")) {


                    startActivity(new Intent(getApplicationContext(),ChatHere.class));
                }

                else if (items[item].equals("Cancel")) {


                    dialog.dismiss();
                }
            }

        });
        builder.show();
    }
}