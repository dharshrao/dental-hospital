from pyodide.ffi import create_proxy
from pyscript import document, window
import js

# Mobile Navigation Toggle
nav_toggle = document.querySelector('.nav-toggle')
nav_links = document.querySelector('.nav-links')

def toggle_nav(event):
    nav_links.classList.toggle('active')
    icon = nav_toggle.querySelector('i')
    if nav_links.classList.contains('active'):
        icon.classList.remove('fa-bars')
        icon.classList.add('fa-times')
    else:
        icon.classList.remove('fa-times')
        icon.classList.add('fa-bars')

if nav_toggle:
    nav_toggle.addEventListener('click', create_proxy(toggle_nav))

# Sticky Navbar
navbar = document.querySelector('.navbar')

def on_scroll(event):
    if window.scrollY > 50:
        navbar.classList.add('scrolled')
    else:
        navbar.classList.remove('scrolled')

window.addEventListener('scroll', create_proxy(on_scroll))

# Intersection Observer for Scroll Animations
faders = document.querySelectorAll('.fade-in')

def handle_intersect(entries, observer):
    for entry in entries:
        if entry.isIntersecting:
            entry.target.classList.add('appear')
            observer.unobserve(entry.target)

options = js.Object.new()
options.threshold = 0.15
options.rootMargin = "0px 0px -50px 0px"

appearOnScroll = window.IntersectionObserver.new(create_proxy(handle_intersect), options)

for fader in faders:
    appearOnScroll.observe(fader)

# Before/After Slider Logic
teeth_slider = document.getElementById("teeth-slider")
ba_after = document.getElementById("ba-after")
slider_line = document.getElementById("slider-line")

def handle_slider(event):
    val = str(teeth_slider.value) + "%"
    ba_after.style.clipPath = f"polygon(0 0, {val} 0, {val} 100%, 0 100%)"
    slider_line.style.left = val

if teeth_slider:
    teeth_slider.addEventListener("input", create_proxy(handle_slider))
