from lib.booking_manager import BookingManager
from lib.donation_manager import DonationManager
from lib.location_manager import LocationManager
from lib.user_manager import UserManager



home_page_content = {
    "meta": {
        "page_title":"Prophet Yani - Spiritual Guidance and Charity",
    },
    "hero": {
        "title": "Empowering Lives Through Spiritual Guidance and Charity",
        "subtitle": "Join Prophet Yani in a journey of enlightenment and compassion. Your contributions foster global goodwill and personal growth.",
        "buttons": [
            {
                "text": "Book your Consultation", 
                "type": "primary",
                "action_type": "email",
                "target": "ProphetYani@gmail.com"
            },
            {
                "text": "Make a Difference", 
                "type": "secondary",
                "action_type": "link",
                "target": "https://www.paypal.com/paypalme/tip69"
            }
        ]
    },
    "problem_solution_section": {
        "title": "Navigating Life's Journey: Challenges and Pathways",
        "problems": [
            {
                "title": "Seeking Harmony in Chaos",
                "description": "In a world brimming with uncertainties and challenges, finding inner peace and purpose can seem elusive. You may feel overwhelmed by ".title() + "Life's " + "complexities, struggling to find solace in the midst of chaos. The quest for spiritual guidance and emotional balance is more pressing than ever, yet the path to enlightenment remains clouded for many.".title(),
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/problem-1.png"
            },
            {
                "title": "The Quest for Meaning",
                "description": "Without guidance, these feelings of unrest and disconnection can grow, leaving you more lost in the intricacies of life. The absence of spiritual alignment not only affects your inner peace but also hinders your ability to contribute positively to the world around you. The gap between your current state and where you aspire to be in your spiritual journey can widen, making the search for meaning and fulfillment increasingly difficult.".title(),
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/problem-2.png"
            },
            {
                "title": "Illuminating Your Path",
                "description": "Prophet Yani offers a beacon of light in this journey. Through personalized spiritual consultations and guidance, you can navigate these turbulent times with wisdom and clarity. Our approach blends ancient wisdom with modern understanding, providing you with the tools and insights needed for personal growth and enlightenment. By joining our community, you not only embark on a path to self-discovery but also contribute to a greater cause, as your participation aids in our charitable missions worldwide. Begin your transformative journey today and find the peace and purpose you seek.".title(),
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/problem-3.png"
            }
        ]
    },
    "benefits_section": {
        "title": "How Our Services Transform Lives",
        "benefits": [
            {
                "title": "Personal and Spiritual Transformation",
                "features": "Customized Spiritual Consultations",
                "description": "One-on-one sessions tailored to your unique spiritual journey, offering specific insights and guidance...",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/benefits-1.png",
                "impact": "Achieve lasting inner peace, heightened self-awareness, and a clearer life path."
            },
            {
                "title": "Community of Compassion and Support",
                "features": "Access to an Exclusive Online Community Platform",
                "description": "Join an online forum where members share experiences, insights, and support, fostering a sense of belonging...",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/benefits-2.png",
                "impact": "Gain emotional support, build meaningful connections, and be part of a collective journey."
            },
            {
                "title": "Contribution to a Greater Cause",
                "features": "Integrated Charitable Giving Options",
                "description": "With each consultation, contribute to a range of charitable causes, impacting the wider world positively...",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/benefits-3.png",
                "impact": "Experience the fulfillment of personal growth while contributing to global goodwill and change."
            }
            # Add more benefits as needed
        ]
    },
    "social_proof_section": {
        "title": "Our Impact and Recognition",
        "testimonials": [
            {
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/testamonial-1.webp",
                "alt_text": "Client Testimonial",
                "author": "Emma K., Health Professional",
                "quote": "Prophet Yani's guidance has been a transformative experience..."
            },
            {
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/testamonial-2.webp",
                "alt_text": "Client Testimonial",
                "author": "Raj P., Entrepreneur",
                "quote": "Joining Prophet Yani's community has opened new avenues of growth and connection..."
            },
            {
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/testamonial-3.webp",
                "alt_text": "Client Testimonial",
                "author": "Luisa G., Artist",
                "quote": "The blend of spirituality and practical wisdom is truly unique..."
            }
        ],
        "success_stories": [
            {
                "title": "John's Story",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/success-1.webp",
                "alt_text": "John's Success Story",
                "description": "John's journey is a testament to personal transformation. His story of overcoming life's hurdles with the help of spiritual guidance has inspired many. From feeling lost and disoriented, John has found a new direction and purpose in life..."
            },
            {
                "title": "Maria's Transformation",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/success-2.webp",
                "alt_text": "Maria's Transformation",
                "description": "Maria's story is one of remarkable change, from skepticism to becoming an active and engaged community member. Her transformation highlights the impact of spiritual connection and community support in rediscovering life's joys and meanings..."
            }
        ],
        # "media_features": [
        #     {
        #         "title": "The Spiritual Herald",
        #         "description": "Featured for innovative approaches in spiritual guidance and community building...",
        #         "image_url": "https://placekitten.com/g/64/64",
        #         "alt_text": "The Spiritual Herald Logo"
        #     },
        #     {
        #         "title": "Mindful Living Magazine",
        #         "description": "Recognized for contributions to mindful living practices and holistic well-being...",
        #         "image_url": "https://placekitten.com/g/65/65",
        #         "alt_text": "Mindful Living Magazine Logo"
        #     }
        # ],
        "partnerships": [
            {
                "title": "Zodiac Psychics",
                "feature_offering": "Personalized psychic readings and spiritual consultations.",
                "unique_value": "Dive into a world of intuitive guidance and self-discovery with Prophet Yani, enhancing your spiritual journey.",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/home_zodiac.png",
                "url": "https://zodiacempress.com/"
            },
        ],
        "social_media_highlights": {
            "followers": [
                {
                    "name": "Bigo",
                    "icon": "svg",
                    "icon_svg": "images/bigo-live.svg",
                    "count": "15000",
                    "url": "https://www.bigo.tv/en/sugarbabycam"
                },
                {
                    "name": "Instagram",
                    "icon": "fab fa-instagram",
                    "count": "1300",
                    "url": "https://www.instagram.com/yani.vip/",
                    "color":"#E4405F"
                },
                {
                    "name": "TikTok",
                    "icon": "fab fa-tiktok",
                    "count": "1062",
                    "url": "https://www.tiktok.com/@zodiac_empress",
                    "color":"#25F4EE"
                },
                {
                    "name": "Twitter",
                    "icon": "fab fa-twitter",
                    "count": "64",
                    "url": "https://www.youtube.com/yaniwhite",
                    "color":"#1DA1F2"
                },
                {
                    "name": "YouTube",
                    "icon": "fab fa-youtube",
                    "count": "16",
                    "url": "https://www.youtube.com/yaniwhite",
                    "color":"#FF0000"
                }
            ]
        },

        "impact_statistics": [
            {
                "name": "Consultations",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/impact-1.webp",
                "alt_text": "Consultations Statistic",
                "count": "",
                "description": "Individual consultations conducted"
            },
            {
                "name": "Donations",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/impact-2.webp",
                "alt_text": "Donations Statistic",
                "count": "",
                "description": "Contributed to charitable causes"
            },
            {
                "name": "Global Impact",
                "image_url": "https://jonathanksullivan.github.io/prophet-yani/image/impact-3.webp",
                "alt_text": "Global Impact Statistic",
                "count": "",
                "description": "Countries positively impacted"
            }
        ]
    },
    "features_section": {
        "title": "Our Unique Features",
        "features": [
            {
                "title": "Personalized Spiritual Consultations",
                "description": "Embark on a journey tailored uniquely to you, where every session is a step closer to self-discovery and inner peace. Our approach is deeply personal, focusing on your individual spiritual needs and aspirations."
            },
            {
                "title": "Global Online Community Access",
                "description": "Join a vibrant global community that nurtures your spiritual growth. Engage in meaningful conversations, share experiences, and gain insights from like-minded souls on similar spiritual paths."
            },
            {
                "title": "Diverse Charitable Initiatives",
                "description": "Transform lives by contributing to various charitable causes. Your journey with us extends beyond personal growth, making a real-world impact in communities around the globe."
            },
            {
                "title": "Flexible Consultation Formats",
                "description": "Choose the consultation style that fits your life, be it in-person, online, or in group settings. Our flexible approach ensures that spiritual guidance is always within your reach, no matter where you are."
            },
            {
                "title": "Expert Guidance Backed by Experience",
                "description": "Benefit from the extensive experience and profound wisdom of Prophet Yani. Our guidance is rooted in years of practice and success, offering you a pathway to spiritual clarity and fulfillment."
            }
        ]
    },
    "faq_section": {
        "title": "Frequently Asked Questions",
        "faqs": [
            {
                "question": "What makes Prophet Yani's spiritual guidance unique compared to other services?",
                "answer": "Prophet Yani's guidance is deeply personalized, blending ancient spiritual wisdom with modern life realities..."
            },
            {
                "question": "I’m new to spiritual guidance. Is this suitable for beginners?",
                "answer": "Absolutely! Prophet Yani's services are designed to be accessible..."
            },
            {
                "question": "How can I be sure my contributions are going to the stated charitable causes?",
                "answer": "Transparency is a cornerstone of our service..."
            },
            {
                "question": "Are there any proven results or success stories from Prophet Yani’s consultations?",
                "answer": "Yes, numerous clients have reported significant positive changes..."
            },
            {
                "question": "What if I can’t attend the consultations in person?",
                "answer": "No problem at all. We offer flexible consultation formats..."
            },
            {
                "question": "Can spiritual guidance really make a difference in my day-to-day life?",
                "answer": "Definitely. Our clients often find that the insights..."
            },
            {
                "question": "Is the online community active and supportive?",
                "answer": "Yes, our online community is a vibrant and supportive space..."
            },
            {
                "question": "How often are new spiritual topics discussed?",
                "answer": "We regularly update our content and discussions to cover a wide range of spiritual topics, ensuring relevance and depth."
            },
            {
                "question": "Can I contribute my experiences to the community?",
                "answer": "Absolutely! We encourage sharing personal experiences as they can be incredibly insightful and inspiring for others."
            },
            {
                "question": "Are there any offline events or meetups?",
                "answer": "Yes, we organize offline events and meetups periodically to foster a stronger sense of community and personal connection."
            },
            {
                "question": "What is the process for booking a private consultation?",
                "answer": "Booking a private consultation is easy. Simply visit our consultation page, choose an available slot, and make your appointment."
            },
            {
                "question": "How can I stay updated with new offerings and updates?",
                "answer": "The best way to stay informed is by subscribing to our newsletter and following us on our social media channels."
            },
            {
                "question": "How often are new spiritual topics discussed?",
                "answer": "We regularly update our content and discussions to cover a wide range of spiritual topics, ensuring relevance and depth."
            },
            {
                "question": "Can I contribute my experiences to the community?",
                "answer": "Absolutely! We encourage sharing personal experiences as they can be incredibly insightful and inspiring for others."
            },
            {
                "question": "Are there any offline events or meetups?",
                "answer": "Yes, we organize offline events and meetups periodically to foster a stronger sense of community and personal connection."
            },
            {
                "question": "What is the process for booking a private consultation?",
                "answer": "Booking a private consultation is easy. Simply visit our consultation page, choose an available slot, and make your appointment."
            },
            {
                "question": "How can I stay updated with new offerings and updates?",
                "answer": "The best way to stay informed is by subscribing to our newsletter and following us on our social media channels."
            },
            {
                "question": "Are there any resources available for self-guided learning?",
                "answer": "Yes, we offer a variety of resources, including articles, videos, and guided meditations for those interested in self-guided spiritual learning."
            },
            {
                "question": "Do you offer group sessions or workshops?",
                "answer": "We do offer group sessions and workshops, which are great opportunities for collective learning and sharing experiences with others."
            }
        ]
    },
    "footer": {
        "text": "&copy; 2023 prophetyani.com. All rights reserved."
    }
}


about_page_content = {
    "meta": {
        "page_title": "Prophet Yani - Spiritual Guidance and Charity",
    },
    "content": {
        "title": "Seeking Inner Wisdom: The Journey of Prophet Yani",
        "header_image": {
            "url": "https://jonathanksullivan.github.io/prophet-yani/image/about.png",
            "alt_text": "Prophet Yani - Spiritual Guide"
        },
        "header_image_background": {
            "url": "https://jonathanksullivan.github.io/prophet-yani/image/about-back.webp",
            "alt_text": "Prophet Yani - Spiritual Guide"
        },
        "sections": [
            {
                "title": "The Transformation Odyssey",
                "content": "Prophet Yani's story is one of transformation, shaped by personal challenges and a profound quest for understanding. Her empathetic approach to guiding others stems from this rich journey. Embracing both evidence-based practices and spiritual wisdom, she tailors her guidance to the unique journeys of her clients."
            },
            {
                "title": "Guided by Wisdom and Recognition",
                "content": "As an ordained minister and a certified spiritual guide, Prophet Yani combines recognized qualifications with deep spiritual insight. This unique blend reflects her commitment to ethical, compassionate spiritual leadership. Her dedication to continuous learning and excellence shines through in her guidance, fostering trust and integrity in the journey toward enlightenment and inner peace."
            },
            {
                "title": "Empowering Lives and Spirits",
                "content": "In sessions, clients find a haven for growth and self-discovery. They leave with practical tools and insights, feeling heard, understood, and empowered to face life's challenges with newfound resilience and clarity."
            },
            {
                "title": "Voices of Gratitude",
                "content": "Testimonial: “During a pivotal moment, the session offered me renewed hope and a clear direction, which was invaluable.”"
            },
            {
                "title": "Transforming Stats",
                "content": "A majority of clients report significant self-improvement and better life management after sessions."
            }
        ]
    },
    "footer": {
        "text": "&copy; 2023 prophetyani.com. All rights reserved."
    }
}

register_page_content = {
    "meta": {
        "page_title":"Prophet Yani - Spiritual Guidance and Charity",
    },
    "footer": {
        "text": "&copy; 2023 prophetyani.com. All rights reserved."
    }
}

login_page_content = {
    "meta": {
        "page_title":"Prophet Yani - Spiritual Guidance and Charity",
    },
    "footer": {
        "text": "&copy; 2023 prophetyani.com. All rights reserved."
    }
}

profile_page_content = {
    "meta": {
        "page_title":"Prophet Yani - Spiritual Guidance and Charity",
    },
    "footer": {
        "text": "&copy; 2023 prophetyani.com. All rights reserved."
    }
}

user_dashboard_page_content = {
    "meta": {
        "page_title":"Prophet Yani - Spiritual Guidance and Charity",
    },
    "footer": {
        "text": "&copy; 2023 prophetyani.com. All rights reserved."
    }
}


confirm_booking_page_content = {
    "meta": {
        "page_title":"Prophet Yani - Spiritual Guidance and Charity",
    },
    "footer": {
        "text": "&copy; 2023 prophetyani.com. All rights reserved."
    }
}
