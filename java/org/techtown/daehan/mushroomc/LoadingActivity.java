package org.techtown.daehan.mushroomc;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.TextView;

public class LoadingActivity extends AppCompatActivity {

    TextView tv1;
    TextView tv2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);

        tv1 = findViewById(R.id.textView2);
        tv2 = findViewById(R.id.textView3);

        Animation ani = AnimationUtils.loadAnimation(this, R.anim.loadingsplash);

        tv1.startAnimation(ani);
        tv2.startAnimation(AnimationUtils.loadAnimation(this, R.anim.loadingsplash2));

        Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent intent = new Intent(getApplicationContext(),ResultActivity.class);
                startActivity(intent);
                //mediaPlayer.pause();
                finish();
            }

        },10000);

    }
}
