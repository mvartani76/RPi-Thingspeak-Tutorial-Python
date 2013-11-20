RPi-Thingspeak-Tutorial-Python
==============================

Simple python files to demonstrate ThingSpeak. Portions taken from http://www.australianrobotics.com.au/news/how-to-talk-to-thingspeak-with-python-a-memory-cpu-monitor.

Register with ThingSpeak
========================
Go to https://www.thingspeak.com/ and follow the instructions.

Install Python Libraries
========================
<pre class="code-text-only" style="display: none;">
<code>sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev
sudo apt-get build-dep python</code></pre>

Install psutil
==============
<pre class="code-text-only" style="display: none;">
<code>sudo easy_install psutil</code></pre>

Git the Code from Github
========================
<pre class="code-text-only" style="display: none;">
<code>sudo git clone https://github.com/mvartani76/RPi-Thingspeak-Tutorial-Python/</code></pre>

Remember to change the API KEY to your key that was generated for you in Thingspeak

<b>pushtothingspeak.py -</b> this file pushs one single value to ThingSpeak.<br>
<b>thingspeak_cpu_loop.py -</b> this file continously pushes the CPU load and available memory from the Pi every 16 seconds.
