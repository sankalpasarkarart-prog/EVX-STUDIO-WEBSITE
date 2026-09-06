import re
import os

with open('terms.html', 'r', encoding='utf-8') as f:
    terms_html = f.read()

# Extract header (up to </nav>)
header_match = re.search(r'(.*?</nav>)', terms_html, re.DOTALL)
header = header_match.group(1)

# Extract footer and scripts
footer_match = re.search(r'(<!-- ======== FOOTER ======== -->.*)', terms_html, re.DOTALL)
footer = footer_match.group(1)

founder_content = '''
    <style>
        .about-content {
            max-width: 900px;
            margin: 150px auto 4rem;
            padding: 0 1.5rem;
            color: var(--text-secondary);
            line-height: 1.8;
            font-size: 1.1rem;
        }
        .founder-profile {
            text-align: center;
            margin-bottom: 3rem;
        }
        .founder-img {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid var(--accent);
            padding: 5px;
            box-shadow: 0 10px 30px rgba(var(--accent-rgb), 0.3);
            margin-bottom: 1.5rem;
        }
        .founder-name {
            font-family: var(--font-heading);
            font-size: 2.5rem;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }
        .founder-title {
            color: var(--accent);
            font-weight: 500;
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }
        .founder-location {
            color: var(--text-muted);
            font-size: 1rem;
        }
        .founder-story {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            padding: 3rem;
            border-radius: var(--radius-card);
            backdrop-filter: blur(20px);
        }
        .founder-story p {
            margin-bottom: 1.5rem;
        }
    </style>

    <main class="about-content animate-in">
        <div class="founder-profile">
            <img src="assets/founder.jpg" alt="Sankalpa Sarkar (ESHAN)" class="founder-img">
            <h1 class="founder-name">Sankalpa Sarkar (ESHAN)</h1>
            <div class="founder-title">Senior Motion Graphics Artist & Founder of EVX STUDIO</div>
            <div class="founder-location"><i class="ri-map-pin-line"></i> West Bengal, India</div>
        </div>

        <div class="founder-story glass-strong">
            <p>Hi, I’m Eshan. Before I was ever rendering keyframes or managing timelines, my world was built entirely out of water and pigment. For over 12 years, I have been a dedicated watercolor artist. That foundation gave me an incredibly deep appreciation for composition, design, color theory, and visual storytelling—skills that you can't just learn from a software manual.</p>
            
            <p>My journey into the digital space actually started on YouTube. I wanted to share my watercolor paintings with the world, which meant I had to figure out how to film and edit my own videos. What started as a necessity quickly turned into an absolute passion. I found myself completely captivated by the art of video editing, motion graphics, and animation. I started diving deep into software like Premiere Pro, After Effects, DaVinci Resolve, Adobe Animate, Photoshop, and Affinity.</p>
            
            <p>The more I edited, the more I realized that manipulating pixels on a screen felt just like putting brush strokes on a canvas. The medium had changed, but the art remained the same. That realization led to the birth of EVX STUDIO.</p>
            
            <p>I also have a deep, underlying interest in technology. In fact, the very website you're scrolling through right now was designed and built by me. I love creating seamless, premium experiences, whether that’s in a 30-second viral short, a complex 3D animation, or the code that powers this site.</p>
            
            <p>At EVX STUDIO, I blend traditional artistic principles with cutting-edge tech to create visuals that don't just look good, but genuinely connect with people. Thanks for stopping by, and I can't wait to see what we create together.</p>
        </div>
    </main>
'''

founder_html = header.replace('<title>Terms and Conditions', '<title>Know About the Founder') + founder_content + footer

with open('know-about-the-founder.html', 'w', encoding='utf-8') as f:
    f.write(founder_html)

about_us_content = '''
    <style>
        .about-content {
            max-width: 900px;
            margin: 150px auto 4rem;
            padding: 0 1.5rem;
            color: var(--text-secondary);
            line-height: 1.8;
            font-size: 1.1rem;
        }
        .about-header {
            text-align: center;
            margin-bottom: 3rem;
        }
        .about-title {
            font-family: var(--font-heading);
            font-size: 3rem;
            color: var(--text-primary);
            margin-bottom: 1rem;
        }
        .about-subtitle {
            color: var(--accent);
            font-weight: 500;
            font-size: 1.3rem;
            max-width: 700px;
            margin: 0 auto;
        }
        .process-box {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.05);
            padding: 3rem;
            border-radius: var(--radius-card);
            backdrop-filter: blur(20px);
            margin-bottom: 2rem;
        }
        .process-box h3 {
            color: var(--text-primary);
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .process-box h3 i {
            color: var(--accent);
        }
        .process-step {
            display: flex;
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        .step-number {
            background: rgba(var(--accent-rgb), 0.1);
            color: var(--accent);
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            flex-shrink: 0;
            font-family: var(--font-heading);
        }
    </style>

    <main class="about-content animate-in">
        <div class="about-header">
            <h1 class="about-title">Know About Us</h1>
            <div class="about-subtitle">We are EVX Studio. A powerhouse team of 15+ artists, designers, 2D/3D animators, video editors, and motion graphics experts.</div>
        </div>

        <div class="process-box glass-strong">
            <h3><i class="ri-team-line"></i> Our Team & Leadership</h3>
            <p>Every single order at EVX STUDIO is personally handled by our founder, Eshan. He either creates and edits the video himself, or directly manages our elite editors, providing strict creative direction to ensure the final product meets our premium standards.</p>
            <p>Beyond our editing talent, we have dedicated scriptwriters, content strategists, and managers who handle end-to-end social media profiles for our clients.</p>
        </div>

        <div class="process-box glass-strong">
            <h3><i class="ri-flow-chart"></i> How We Process Orders</h3>
            
            <div class="process-step">
                <div class="step-number">1</div>
                <div>
                    <strong>Strategy & Blueprint</strong><br>
                    First, our content strategist analyzes the market and creates a comprehensive pathway for us to follow. They provide the initial instructions and creative direction for the campaign.
                </div>
            </div>
            
            <div class="process-step">
                <div class="step-number">2</div>
                <div>
                    <strong>Scripting</strong><br>
                    We ask the client for their topic or core message. Our dedicated scriptwriters then craft an engaging, highly informative, and retention-optimized script.
                </div>
            </div>
            
            <div class="process-step">
                <div class="step-number">3</div>
                <div>
                    <strong>Production & Editing</strong><br>
                    If your plan includes a shoot, our team handles it on-site. If not, you provide the raw data or footage, and we get to work. The best video editors on our team meticulously process your videos under the direct supervision of the founder.
                </div>
            </div>
            
            <div class="process-step">
                <div class="step-number">4</div>
                <div>
                    <strong>Review & Revisions</strong><br>
                    When the video is ready, we share it with you. We stand firmly by our work. If you want any adjustments, we provide revisions. If we ever make a mistake or fall short of our promise, we will give you a free revision or a full refund. We care deeply about client satisfaction.
                </div>
            </div>
            
            <div class="process-step">
                <div class="step-number">5</div>
                <div>
                    <strong>Final Delivery</strong><br>
                    Our QA team thoroughly checks every frame, audio channel, and graphic before finalizing and completing the order.
                </div>
            </div>
        </div>
    </main>
'''

about_us_html = header.replace('<title>Terms and Conditions', '<title>Know About Us') + about_us_content + footer

with open('know-about-us.html', 'w', encoding='utf-8') as f:
    f.write(about_us_html)
print('Pages created.')
