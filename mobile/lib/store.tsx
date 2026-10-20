import React, {createContext, useContext, useEffect, useMemo, useState} from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as Linking from 'expo-linking';

export const colors = {ink:'#171817', orange:'#ef5b2a', cream:'#f7f3eb', paper:'#fffdf8', muted:'#72736d', line:'#e7e0d5', yellow:'#f5c451'};
export const products = [
  {id:'margherita', name:'بيتزا مارغريتا', description:'صلصة طماطم، موزاريلا، ريحان طازج', category:'بيتزا', emoji:'🍕', prices:{S:14,M:20,L:38,XL:50}},
  {id:'veggie', name:'بيتزا خضار', description:'فلفل ملون، زيتون، بصل، ذرة وفطر', category:'بيتزا', emoji:'🥬', prices:{S:15,M:22,L:36,XL:48}},
  {id:'salami', name:'بيتزا سلامي', description:'سلامي، موزاريلا وصلصة البيت الخاصة', category:'بيتزا', emoji:'🍕', prices:{S:17,M:25,L:42,XL:55}},
  {id:'tuna', name:'بيتزا تونة', description:'تونة، بصل، زيتون وموزاريلا', category:'بيتزا', emoji:'🐟', prices:{S:15,M:23,L:40,XL:53}},
  {id:'calzone', name:'كلزوني', description:'عجينة محشوة بالجبنة واللحم', category:'بيتزا', emoji:'🥟', prices:{S:18,M:28,L:45,XL:60}},
  {id:'fries', name:'بطاطا كبيرة', description:'مقرمشة ومملحة، مثالية للمشاركة', category:'جانبيات', emoji:'🍟', prices:{normal:10}},
  {id:'wings', name:'أجنحة دجاج', description:'6 قطع مع صوص من اختيارك', category:'جانبيات', emoji:'🍗', prices:{normal:20}},
  {id:'cola', name:'كولا 1.25 لتر', description:'باردة وجاهزة مع طلبك', category:'مشروبات', emoji:'🥤', prices:{normal:4}}
] as const;
type Product = typeof products[number];
export type CartItem = {key:string; product:Product; variant:string; price:number; qty:number};
type Member = {name:string; phone:string; points:number; consent:boolean};
type StoreContextValue = {cart:CartItem[]; member:Member|null; add:(product:Product, variant:string)=>void; remove:(key:string)=>void; cartTotal:number; cartCount:number; join:(name:string,phone:string,consent:boolean)=>void; redeem:(cost:number,name:string)=>boolean; orderOnWhatsApp:()=>void};
const StoreContext = createContext<StoreContextValue>({} as StoreContextValue);
export function StoreProvider({children}:{children:React.ReactNode}){
 const [cart,setCart]=useState<CartItem[]>([]); const [member,setMember]=useState<Member|null>(null);
 useEffect(()=>{AsyncStorage.multiGet(['cart','member']).then(([c,m])=>{if(c[1])setCart(JSON.parse(c[1]));if(m[1])setMember(JSON.parse(m[1]));});},[]);
 useEffect(()=>{AsyncStorage.setItem('cart',JSON.stringify(cart));},[cart]); useEffect(()=>{if(member)AsyncStorage.setItem('member',JSON.stringify(member));},[member]);
 const value=useMemo(()=>({cart,member,add:(product:Product,variant:string)=>{const price=product.prices[variant as keyof typeof product.prices] as number;setCart(x=>{const key=`${product.id}-${variant}`;const old=x.find(i=>i.key===key);return old?x.map(i=>i.key===key?{...i,qty:i.qty+1}:i):[...x,{key,product,variant,price,qty:1}];});},remove:(key:string)=>setCart(x=>x.filter(i=>i.key!==key)),cartTotal:cart.reduce((a,i)=>a+i.price*i.qty,0),cartCount:cart.reduce((a,i)=>a+i.qty,0),join:(name:string,phone:string,consent:boolean)=>setMember({name,phone,points:50,consent}),redeem:(cost:number,name:string)=>{if(!member||member.points<cost)return false;setMember({...member,points:member.points-cost});return true;},orderOnWhatsApp:()=>{const lines=['مرحبًا Pizza Hot، أريد تأكيد هذا الطلب:','',...cart.map(i=>`• ${i.product.name} (${i.variant}) × ${i.qty} — ${i.price*i.qty}₪`),'',`الإجمالي: ${cart.reduce((a,i)=>a+i.price*i.qty,0)}₪`,member?`عضو نقاط: ${member.name} — ${member.phone}`:'','الاسم: ','العنوان: '];Linking.openURL(`https://wa.me/972569787731?text=${encodeURIComponent(lines.join('\n'))}`);}}),[cart,member]);
 return <StoreContext.Provider value={value}>{children}</StoreContext.Provider>;
}
export const useStore=()=>useContext(StoreContext);
