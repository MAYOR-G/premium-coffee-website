import { motion } from 'framer-motion';
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
