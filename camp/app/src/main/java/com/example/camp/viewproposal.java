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

public class viewproposal extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {

    ListView l1;
    SharedPreferences sh;
    String[] details,proposal_id,amount,date,value,statu,email,booking_id;
    public static String pid,amt,bid,stat;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_viewproposal);


        l1=(ListView) findViewById(R.id.list);
        l1.setOnItemClickListener(this);
        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());


        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) viewproposal.this;
        String q = "/viewproposal?log_id=" +sh.getString("login_id", "")+"&bid="+viewbookings.bid;
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


                date = new String[ja1.length()];
                amount = new String[ja1.length()];
                statu = new String[ja1.length()];

                booking_id= new String[ja1.length()];

                proposal_id= new String[ja1.length()];
                value = new String[ja1.length()];


                for (int i = 0; i < ja1.length(); i++) {



                    date[i] = ja1.getJSONObject(i).getString("date");
                    amount[i] = ja1.getJSONObject(i).getString("amount");
                    statu[i] = ja1.getJSONObject(i).getString("status");
                    proposal_id[i] = ja1.getJSONObject(i).getString("proposal_id");



                    booking_id[i] = ja1.getJSONObject(i).getString("booking_id");

                    value[i] =  " date: " + date[i] + "\n amount: " + amount[i]  + "\n status: " + statu[i]   ;

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
        pid=proposal_id[i];
        amt=amount[i];
        bid=booking_id[i];
        stat=statu[i];



        if (stat.equalsIgnoreCase("pending")) {
            final CharSequence[] items = {"accept","reject", "Cancel"};

            AlertDialog.Builder builder = new AlertDialog.Builder(viewproposal.this);
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {

                    if (items[item].equals("accept")) {


                        JsonReq JR = new JsonReq();
                        JR.json_response = (JsonResponse) viewproposal.this;
                        String q = "/accept?log_id=" + sh.getString("login_id", "") + "&pid=" + pid;
                        q = q.replace(" ", "%20");
                        JR.execute(q);
                    } else if (items[item].equals("reject")) {


                        JsonReq JR = new JsonReq();
                        JR.json_response = (JsonResponse) viewproposal.this;
                        String q = "/reject?log_id=" + sh.getString("login_id", "") + "&pid=" + pid;
                        q = q.replace(" ", "%20");
                        JR.execute(q);
                    }
                }

            });
            builder.show();

        }else if (stat.equalsIgnoreCase("accept")) {
            final CharSequence[] items = {"make payment"};

            AlertDialog.Builder builder = new AlertDialog.Builder(viewproposal.this);
            builder.setItems(items, new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int item) {

                    if (items[item].equals("make payment")) {


                        startActivity(new Intent(getApplicationContext(), makepayment.class));


                    }
                }

            });
            builder.show();
        }
    }


    }
