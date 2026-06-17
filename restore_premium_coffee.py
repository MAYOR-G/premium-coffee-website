import os

files = {}

files["tailwind.config.js"] = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'brand-black': '#0a0a0a',
        'brand-charcoal': '#1a1a1a',
        'brand-cream': '#f4f1eb',
        'brand-accent': '#e63946',
        'brand-beige': '#d5c7b3',
      },
      fontFamily: {
        heading: ['Oswald', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
        accent: ['Playfair Display', 'serif'],
      }
    },
  },
  plugins: [],
}
"""

files["src/index.css"] = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Oswald:wght@500;600;700&family=Playfair+Display:ital,wght@1,600&display=swap');

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply font-body bg-brand-black text-brand-cream antialiased overflow-x-hidden;
  }
  h1, h2, h3, h4, h5, h6 {
    @apply font-heading uppercase tracking-wide;
  }
}

.text-stroke {
  -webkit-text-stroke: 1px #f4f1eb;
  color: transparent;
}
.text-stroke-hover:hover {
  color: #f4f1eb;
}
"""

files["src/data/siteContent.ts"] = """export const siteContent = {
  hero: {
    headline: "THE HOME OF",
    accent: "BETTER",
    headlineEnd: "COFFEE",
    subtext: "Ethically sourced, carefully roasted, and delivered fresh to your door. Experience coffee the way it was meant to be.",
    cta: "SHOP COFFEE"
  },
  products: [
    { name: "Ethiopia Yirgacheffe", notes: "Jasmine, Peach, Black Tea", price: "$22", image: "https://images.unsplash.com/photo-1559525839-b184a4d698c7?auto=format&fit=crop&q=80&w=800" },
    { name: "Colombia Supremo", notes: "Chocolate, Caramel, Apple", price: "$19", image: "https://images.unsplash.com/photo-1587734195503-904fca47e0e9?auto=format&fit=crop&q=80&w=800" },
    { name: "Espresso Blend", notes: "Dark Chocolate, Hazelnut", price: "$20", image: "https://images.unsplash.com/photo-1589396575653-c09c794fa6a1?auto=format&fit=crop&q=80&w=800" },
    { name: "Guatemala Antigua", notes: "Cocoa, Spices, Floral", price: "$21", image: "https://images.unsplash.com/photo-1558160074-4d7d8bdf4256?auto=format&fit=crop&q=80&w=800" }
  ],
  locations: [
    { city: "London", image: "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&q=80&w=800" },
    { city: "Manchester", image: "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&q=80&w=800" },
    { city: "Birmingham", image: "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&q=80&w=800" },
    { city: "Leeds", image: "https://images.unsplash.com/photo-1600093463592-8e36ae95ef56?auto=format&fit=crop&q=80&w=800" }
  ],
  wholesale: {
    title: "WHOLESALE COFFEE, ROASTED PROPERLY",
    text: "Partner with us to bring exceptional coffee to your café, restaurant, or office. We provide not just beans, but training and support.",
    image1: "https://images.unsplash.com/photo-1611162458324-aae1eb4129a4?auto=format&fit=crop&q=80&w=800",
    image2: "https://images.unsplash.com/photo-1507133750070-4ed7a4501fc6?auto=format&fit=crop&q=80&w=800"
  },
  barista: {
    title: "BARISTA SCHOOL",
    text: "Learn the art of coffee from our master roasters and champion baristas. From basic espresso extraction to advanced latte art.",
    image1: "https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&q=80&w=800",
    image2: "https://images.unsplash.com/photo-1444418185997-1145401101e0?auto=format&fit=crop&q=80&w=800"
  },
  journey: {
    title: "THE JOURNEY",
    text: "From the high-altitude farms of Colombia to our custom roastery in the heart of the city, every bean is treated with uncompromising respect."
  },
  mosaic: {
    storyImg: "https://images.unsplash.com/photo-1498804103079-a6351b050096?auto=format&fit=crop&q=80&w=800",
    subImg: "https://images.unsplash.com/photo-1607681034540-2c46cc71896d?auto=format&fit=crop&q=80&w=800"
  }
}
"""

files["src/components/Navbar.tsx"] = """import { useState, useEffect } from 'react';
import { ShoppingCart, Menu, X } from 'lucide-react';
import { motion } from 'framer-motion';

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`fixed top-0 w-full z-50 transition-all duration-300 ${scrolled ? 'bg-brand-black/90 backdrop-blur-md py-4' : 'bg-transparent py-6'}`}>
      <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
        <div className="text-2xl font-heading font-bold tracking-widest text-brand-cream">
          ROAST & ORIGIN
        </div>
        
        <nav className="hidden md:flex space-x-8 text-sm uppercase tracking-widest">
          <a href="#" className="hover:text-brand-accent transition-colors">Shop</a>
          <a href="#" className="hover:text-brand-accent transition-colors">Wholesale</a>
          <a href="#" className="hover:text-brand-accent transition-colors">Locations</a>
          <a href="#" className="hover:text-brand-accent transition-colors">Story</a>
        </nav>
        
        <div className="flex items-center space-x-6">
          <button className="hidden md:block bg-brand-accent text-white px-6 py-2 uppercase text-xs font-bold tracking-wider hover:bg-white hover:text-brand-black transition-colors">
            Subscribe
          </button>
          <button className="hover:text-brand-accent transition-colors">
            <ShoppingCart size={20} />
          </button>
          <button className="md:hidden hover:text-brand-accent transition-colors" onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
            {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>
      
      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="absolute top-full left-0 w-full bg-brand-charcoal py-8 px-6 flex flex-col space-y-6 md:hidden"
        >
          <a href="#" className="text-xl font-heading hover:text-brand-accent">Shop</a>
          <a href="#" className="text-xl font-heading hover:text-brand-accent">Wholesale</a>
          <a href="#" className="text-xl font-heading hover:text-brand-accent">Locations</a>
          <a href="#" className="text-xl font-heading hover:text-brand-accent">Story</a>
          <button className="bg-brand-accent text-white px-6 py-3 uppercase text-sm font-bold tracking-wider mt-4">
            Subscribe
          </button>
        </motion.div>
      )}
    </header>
  );
}
"""

files["src/components/Hero.tsx"] = """import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center pt-20 px-6 overflow-hidden">
      {/* Background with slight overlay */}
      <div className="absolute inset-0 z-0">
        <div className="absolute inset-0 bg-brand-black/40 z-10" />
        <img 
          src="https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&q=80&w=2000" 
          alt="Coffee Background" 
          className="w-full h-full object-cover grayscale opacity-30"
        />
      </div>

      <div className="relative z-10 max-w-5xl mx-auto text-center flex flex-col items-center">
        <motion.h1 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="text-6xl md:text-8xl lg:text-[10rem] leading-none flex flex-col items-center"
        >
          <span>{siteContent.hero.headline}</span>
          <span className="font-accent text-brand-accent lowercase text-7xl md:text-9xl lg:text-[11rem] -mt-4 md:-mt-8 mb-2 transform -rotate-2">
            {siteContent.hero.accent}
          </span>
          <span>{siteContent.hero.headlineEnd}</span>
        </motion.h1>
        
        <motion.p 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.6 }}
          className="mt-8 max-w-lg text-lg md:text-xl text-brand-cream/80"
        >
          {siteContent.hero.subtext}
        </motion.p>
        
        <motion.button 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.8 }}
          className="mt-12 bg-brand-accent text-white px-10 py-4 uppercase text-sm font-bold tracking-widest hover:bg-white hover:text-brand-black transition-all duration-300"
        >
          {siteContent.hero.cta}
        </motion.button>
      </div>
    </section>
  );
}
"""

files["src/components/Products.tsx"] = """import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function Products() {
  return (
    <section className="py-32 px-6 bg-brand-charcoal">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-end mb-20">
          <h2 className="text-5xl md:text-7xl">Our Coffees</h2>
          <a href="#" className="text-brand-accent uppercase tracking-widest font-bold mt-6 md:mt-0 hover:text-white transition-colors">Shop All Collection →</a>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {siteContent.products.map((product, index) => (
            <motion.div 
              key={index}
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="group cursor-pointer"
            >
              <div className="relative aspect-[3/4] overflow-hidden mb-6 bg-brand-black">
                <img 
                  src={product.image} 
                  alt={product.name} 
                  className="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                />
                <div className="absolute inset-0 border border-brand-cream/10 group-hover:border-brand-accent/50 transition-colors duration-500 m-4" />
              </div>
              <h3 className="text-2xl mb-2">{product.name}</h3>
              <p className="text-brand-cream/60 text-sm uppercase tracking-wider mb-4">{product.notes}</p>
              <div className="flex justify-between items-center">
                <span className="font-body text-lg">{product.price}</span>
                <span className="text-brand-accent text-sm font-bold uppercase tracking-widest opacity-0 group-hover:opacity-100 transition-opacity duration-300">Add to Cart</span>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
"""

files["src/components/CoffeeJourney.tsx"] = """import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function CoffeeJourney() {
  return (
    <section className="py-32 px-6 bg-brand-black overflow-hidden relative">
      {/* Decorative large circle */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] rounded-full border border-brand-cream/5 z-0" />
      
      <div className="max-w-7xl mx-auto relative z-10 flex flex-col md:flex-row items-center">
        <motion.div 
          initial={{ opacity: 0, x: -50 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="w-full md:w-1/2 mb-12 md:mb-0"
        >
          <h2 className="text-6xl md:text-8xl lg:text-[9rem] leading-none text-brand-cream/10 text-stroke">
            THE<br/>JOURNEY
          </h2>
        </motion.div>
        
        <motion.div 
          initial={{ opacity: 0, x: 50 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="w-full md:w-1/2 md:pl-20"
        >
          <p className="text-2xl md:text-3xl leading-relaxed text-brand-cream font-body font-light">
            {siteContent.journey.text}
          </p>
          <button className="mt-12 border-b border-brand-accent text-brand-accent pb-1 uppercase tracking-widest font-bold hover:text-white hover:border-white transition-colors">
            Read Our Story
          </button>
        </motion.div>
      </div>
    </section>
  );
}
"""

files["src/components/Locations.tsx"] = """import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function Locations() {
  return (
    <section className="py-32 px-6 bg-brand-cream text-brand-black">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-6xl md:text-8xl mb-20 text-center">LOCATIONS</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {siteContent.locations.map((loc, index) => (
            <motion.div 
              key={index}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              className="group relative overflow-hidden aspect-square"
            >
              <img 
                src={loc.image} 
                alt={loc.city} 
                className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-700 group-hover:scale-105"
              />
              <div className="absolute inset-0 bg-brand-black/20 group-hover:bg-transparent transition-colors duration-500" />
              <div className="absolute bottom-0 left-0 w-full p-8 bg-gradient-to-t from-brand-black/80 to-transparent">
                <h3 className="text-3xl text-white group-hover:text-brand-accent transition-colors">{loc.city}</h3>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
"""

files["src/components/Wholesale.tsx"] = """import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function Wholesale() {
  return (
    <section className="py-32 px-6 bg-brand-charcoal">
      <div className="max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-16">
        <motion.div 
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="w-full lg:w-5/12"
        >
          <h2 className="text-5xl md:text-7xl mb-8 leading-tight">{siteContent.wholesale.title}</h2>
          <p className="text-lg text-brand-cream/80 mb-12">{siteContent.wholesale.text}</p>
          <button className="bg-white text-brand-black px-8 py-4 uppercase font-bold tracking-widest hover:bg-brand-accent hover:text-white transition-colors duration-300">
            Enquire Now
          </button>
        </motion.div>
        
        <div className="w-full lg:w-7/12 relative mt-16 lg:mt-0">
          <motion.img 
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
            src={siteContent.wholesale.image1} 
            alt="Wholesale Roasting" 
            className="w-full aspect-[4/3] object-cover grayscale"
          />
          <motion.img 
            initial={{ opacity: 0, x: -50, y: 50 }}
            whileInView={{ opacity: 1, x: 0, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.3 }}
            src={siteContent.wholesale.image2} 
            alt="Barista" 
            className="absolute -bottom-16 -left-8 md:-left-16 w-1/2 aspect-square object-cover border-8 border-brand-charcoal shadow-2xl"
          />
        </div>
      </div>
    </section>
  );
}
"""

files["src/components/BaristaSchool.tsx"] = """import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function BaristaSchool() {
  return (
    <section className="py-40 px-6 bg-brand-black">
      <div className="max-w-7xl mx-auto flex flex-col-reverse lg:flex-row items-center gap-16">
        <div className="w-full lg:w-7/12 relative mt-16 lg:mt-0">
          <motion.img 
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
            src={siteContent.barista.image1} 
            alt="Barista Training" 
            className="w-full aspect-[4/3] object-cover"
          />
          <motion.img 
            initial={{ opacity: 0, x: 50, y: -50 }}
            whileInView={{ opacity: 1, x: 0, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.3 }}
            src={siteContent.barista.image2} 
            alt="Latte Art" 
            className="absolute -top-16 -right-8 md:-right-16 w-1/2 aspect-square object-cover border-8 border-brand-black shadow-2xl"
          />
        </div>

        <motion.div 
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="w-full lg:w-5/12 lg:pl-12"
        >
          <h2 className="text-5xl md:text-7xl mb-8 leading-tight">{siteContent.barista.title}</h2>
          <p className="text-lg text-brand-cream/80 mb-12">{siteContent.barista.text}</p>
          <button className="border border-brand-cream text-brand-cream px-8 py-4 uppercase font-bold tracking-widest hover:bg-brand-cream hover:text-brand-black transition-colors duration-300">
            Book a Class
          </button>
        </motion.div>
      </div>
    </section>
  );
}
"""

files["src/components/Mosaic.tsx"] = """import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function Mosaic() {
  return (
    <section className="bg-brand-black">
      <div className="flex flex-col md:flex-row w-full h-[60vh] md:h-[80vh]">
        <motion.a 
          href="#"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          className="group relative w-full md:w-1/2 h-1/2 md:h-full overflow-hidden block"
        >
          <img src={siteContent.mosaic.storyImg} className="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" alt="Our Story" />
          <div className="absolute inset-0 bg-brand-black/40 group-hover:bg-brand-black/20 transition-colors duration-500" />
          <div className="absolute inset-0 flex items-center justify-center">
            <h2 className="text-4xl md:text-6xl font-heading uppercase tracking-widest text-transparent text-stroke group-hover:text-brand-cream transition-colors duration-500">Our Story</h2>
          </div>
        </motion.a>

        <motion.a 
          href="#"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ delay: 0.2 }}
          className="group relative w-full md:w-1/2 h-1/2 md:h-full overflow-hidden block"
        >
          <img src={siteContent.mosaic.subImg} className="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" alt="Subscriptions" />
          <div className="absolute inset-0 bg-brand-black/40 group-hover:bg-brand-black/20 transition-colors duration-500" />
          <div className="absolute inset-0 flex items-center justify-center">
            <h2 className="text-4xl md:text-6xl font-heading uppercase tracking-widest text-transparent text-stroke group-hover:text-brand-cream transition-colors duration-500">Subscriptions</h2>
          </div>
        </motion.a>
      </div>
    </section>
  );
}
"""

files["src/components/NewsletterMarquee.tsx"] = """import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';

export default function NewsletterMarquee() {
  return (
    <section className="bg-brand-accent text-white overflow-hidden py-24">
      <div className="max-w-4xl mx-auto px-6 text-center mb-24">
        <h2 className="text-5xl md:text-7xl mb-6">ALL THE LATEST BREWS</h2>
        <p className="text-lg mb-12 opacity-90">Join our newsletter for fresh roasts, brew guides, and exclusive offers.</p>
        <form className="flex border-b border-white/50 focus-within:border-white pb-2 max-w-md mx-auto transition-colors">
          <input 
            type="email" 
            placeholder="ENTER YOUR EMAIL" 
            className="bg-transparent border-none outline-none flex-grow placeholder-white/50 text-white font-body uppercase tracking-widest"
          />
          <button type="submit" className="hover:translate-x-2 transition-transform">
            <ArrowRight size={24} />
          </button>
        </form>
      </div>

      <div className="w-full flex whitespace-nowrap opacity-50 text-4xl md:text-6xl font-heading uppercase tracking-widest pointer-events-none">
        <motion.div
          animate={{ x: [0, -1035] }}
          transition={{ ease: "linear", duration: 15, repeat: Infinity }}
          className="flex gap-8"
        >
          <span>FRESH ROASTS WEEKLY • SPECIALTY COFFEE • EXPERT BARISTAS • </span>
          <span>FRESH ROASTS WEEKLY • SPECIALTY COFFEE • EXPERT BARISTAS • </span>
          <span>FRESH ROASTS WEEKLY • SPECIALTY COFFEE • EXPERT BARISTAS • </span>
        </motion.div>
      </div>
    </section>
  );
}
"""

files["src/components/Footer.tsx"] = """import { Instagram, Twitter, Facebook } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-brand-charcoal pt-24 pb-12 px-6">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 mb-20">
        <div className="md:col-span-2">
          <h2 className="text-4xl font-heading font-bold tracking-widest text-brand-cream mb-6">ROAST & ORIGIN</h2>
          <p className="text-brand-cream/60 max-w-sm mb-8">
            Roasting exceptional coffee since 2018. From the farm to your cup, we care about every step of the journey.
          </p>
          <div className="flex space-x-4 text-brand-cream/60">
            <a href="#" className="hover:text-brand-accent transition-colors"><Instagram size={24} /></a>
            <a href="#" className="hover:text-brand-accent transition-colors"><Twitter size={24} /></a>
            <a href="#" className="hover:text-brand-accent transition-colors"><Facebook size={24} /></a>
          </div>
        </div>
        
        <div>
          <h4 className="text-sm font-bold uppercase tracking-widest mb-6 text-brand-accent">Shop</h4>
          <ul className="space-y-4 text-brand-cream/80">
            <li><a href="#" className="hover:text-white transition-colors">Single Origin</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Blends</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Equipment</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Subscriptions</a></li>
          </ul>
        </div>
        
        <div>
          <h4 className="text-sm font-bold uppercase tracking-widest mb-6 text-brand-accent">Company</h4>
          <ul className="space-y-4 text-brand-cream/80">
            <li><a href="#" className="hover:text-white transition-colors">Our Story</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Wholesale</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Locations</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
          </ul>
        </div>
      </div>
      
      <div className="max-w-7xl mx-auto pt-8 border-t border-brand-cream/10 flex flex-col md:flex-row justify-between text-xs text-brand-cream/40 uppercase tracking-widest">
        <p>&copy; {new Date().getFullYear()} ROAST & ORIGIN. ALL RIGHTS RESERVED.</p>
        <div className="flex space-x-6 mt-4 md:mt-0">
          <a href="#" className="hover:text-brand-cream transition-colors">Privacy Policy</a>
          <a href="#" className="hover:text-brand-cream transition-colors">Terms of Service</a>
        </div>
      </div>
    </footer>
  );
}
"""

files["src/App.tsx"] = """import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Products from './components/Products';
import CoffeeJourney from './components/CoffeeJourney';
import Locations from './components/Locations';
import Wholesale from './components/Wholesale';
import BaristaSchool from './components/BaristaSchool';
import Mosaic from './components/Mosaic';
import NewsletterMarquee from './components/NewsletterMarquee';
import Footer from './components/Footer';

function App() {
  return (
    <div className="bg-brand-black min-h-screen text-brand-cream font-body selection:bg-brand-accent selection:text-white">
      <Navbar />
      <main>
        <Hero />
        <Products />
        <CoffeeJourney />
        <Locations />
        <Wholesale />
        <BaristaSchool />
        <Mosaic />
        <NewsletterMarquee />
      </main>
      <Footer />
    </div>
  );
}

export default App;
"""

import os
for path, content in files.items():
    print(f"Writing {path}...")
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

