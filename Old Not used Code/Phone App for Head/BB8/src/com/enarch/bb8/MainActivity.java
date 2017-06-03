package com.enarch.bb8;

import java.util.Set;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;


public class MainActivity extends Activity {

	/*Bluetooth*/
	private BluetoothAdapter btAdapter;
	private Set pairedDevices;
	private final static int REQUEST_ENABLE_BT = 1;
	TextView stateBluetooth;
	
	/*Buttons*/
	private Button frustrated;
	private Button giddy;
	private Button maybe;
	private Button no;
	private Button yes;
	private Button yohoo;
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        stateBluetooth = (TextView)findViewById(R.id.bluetoothstate);
        btAdapter = BluetoothAdapter.getDefaultAdapter();
        
        CheckBluetoothState();
        
        setupSoundFrustrated();
        setupSoundGiddy();
        setupSoundMaybe();
        setupSoundNo();
        setupSoundYes();
        setupSoundYohoo();
        
        frustrated.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				
			}
		});
        
        giddy.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				
			}
		});
        
        maybe.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				
			}
		});
        
        no.setOnClickListener(new View.OnClickListener(){
        	
        	@Override
        	public void onClick(View v){
        		
        	}
        });
        
        yes.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				
			}
		});
        
        yohoo.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				
			}
		});
       
    }

    
    private void setupSoundFrustrated() {
    	// Get Refrance to the button
    	frustrated = (Button) findViewById(R.id.frustrated);
    }
    
    private void setupSoundGiddy() {
    	giddy = (Button) findViewById(R.id.giddy);
    }

    private void setupSoundMaybe() {
    	maybe = (Button) findViewById(R.id.maybe);
    } 
    
    private void setupSoundNo() {
    	no = (Button) findViewById(R.id.no);
    }
    
    private void setupSoundYes() {
    	yes = (Button) findViewById(R.id.yes);
    }
    
    private void setupSoundYohoo() {
    	yohoo = (Button) findViewById(R.id.yohoo);
    }
    
    private void CheckBluetoothState() {
    	if (btAdapter == null){
            stateBluetooth.setText("Bluetooth NOT support");
           }else{
            if (btAdapter.isEnabled()){
             if(btAdapter.isDiscovering()){
              stateBluetooth.setText("Bluetooth is currently in device discovery process.");
             }else{
              stateBluetooth.setText("BT is On");
             }
            }else{
             stateBluetooth.setText("BT is Off");
             Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
            }
           }
    }
    
    
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.discoverable) {
        	Intent discoverableIntent = new
        		Intent(btAdapter.ACTION_REQUEST_DISCOVERABLE);
        		discoverableIntent.putExtra(btAdapter.EXTRA_DISCOVERABLE_DURATION, 300);
        		startActivity(discoverableIntent);
        }
        if (id == R.id.insecure_connect_scan) {
        	return true;
        	
        }
        if (id == R.id.secure_connect_scan){
        	return true;
        }
        if (id == R.id.devicesAvalable) {
        	return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
