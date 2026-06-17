import { motion } from 'framer-motion';
import { siteContent } from '../data/siteContent';

export default function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center pt-20 px-6 overflow-hidden">
      {/* Background with slight overlay */}
      <div className="absolute inset-0 z-0 bg-brand-black">
        <div className="absolute inset-0 bg-gradient-to-b from-brand-black/80 via-brand-black/40 to-brand-black z-10" />
        <img 
          src="https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&q=80&w=2000" 
          alt="Coffee Background" 
          className="w-full h-full object-cover opacity-80"
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
