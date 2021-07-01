# standalone atmosphere

A standalone atmosphere shader for SHADERed and shadertoy (https://www.shadertoy.com/view/wlBXWK)

This repo is meant as a way to research and explain a (somewhat simple) atmospheric scattering implementation

Roadmap: 
 - chapman function for approximate optical depth
 - better overall integrator (partly done already)
 - planet shadow
 - multiple scattering

# Plan for the chapman function
A good approximation can be found here: https://zero-radiance.github.io/post/analytic-media/
However, it would be nice to keep this function simple, without any erfc, and sqrt, which could result in a fully analytical atmosphere
https://www.shadertoy.com/view/4lVGRy uses a manual fit to the IE table for precomputed scattering, which might work good enough for this
This: https://www.shadertoy.com/view/XlBfRD renders the atmosphere back to front
What does this allow? alpha blending, effectively you calculate scattering for a segment, then blend it with all segments behind each other
This reduces an exp(-x) you have to put the entire segment scattering into, some other form of order-independant transparency could also work

# Plan for multiple scattering
Space glider (https://www.shadertoy.com/view/MdGfDG) big shader, can be slow to load
already does this, by using the delta-eddington stuff
idk how this works, but it's effectively adding the rayleigh color to the unshadowed part of the atmo
It's kinda hacky but it works

If the above works and a fully analytical atmo is possible, it might be possible to integrate it over an angle, and get multiple scattering from there

