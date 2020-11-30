package org.techtown.daehan.mushroomc;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.drawable.Animatable;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Handler;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class SplashActivity extends AppCompatActivity {

    ImageView iv;
    MediaPlayer mediaPlayer;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        Animation ani = AnimationUtils.loadAnimation(this, R.anim.firstsplash);
        iv = findViewById(R.id.imageView3);
        iv.startAnimation(ani);

        mediaPlayer = MediaPlayer.create(this, R.raw.monkeys);
        mediaPlayer.start();
        Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent intent = new Intent(getApplicationContext(),PhotoActivity.class);
                startActivity(intent);
                mediaPlayer.pause();
                finish();
            }

        },4500);
    }

    @Override
    protected void onPause() {
        super.onPause();
        finish();
    }
}
