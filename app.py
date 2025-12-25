import streamlit as st
import pandas as pd
import time
import random

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Bookies Premium", page_icon="📓", layout="wide")

# Session State Initialization
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 2. PREMIUM CSS (MAGAZINE STYLE - REFINED) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Lato:wght@300;400;700&display=swap');

    /* GENERAL SETTINGS */
    .stApp {
        background-color: #F9F8F6; /* Creamy White */
        color: #1a1a1a;
    }
    
    /* TYPOGRAPHY UPGRADE */
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        font-weight: 600;
        color: #000;
    }
        /* THÊM VÀO PHẦN IMPORT GOOGLE FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lora:wght@400;500;600&display=swap');

    h3 {
        font-family: 'Lora', serif !important;
        font-size: 1.5rem !important;
        font-weight: 600;
        # font-style: italic;
        text-transform: uppercase;
        margin-bottom: 1.8rem !important;
        letter-spacing: 2.2px;
        position: relative;
        display: inline-block;
        color: #1a1a1a;
        padding-left: 15px;
    }

    h3::before {
    content: "›";
    position: absolute;
    left: -15px;
    top: 40%;
    transform: translateY(-50%);
    font-size: 1.75rem;
    color: #000;
    opacity: 1;
}
            

    /* --- HEADER SECTION --- */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 0 30px 0;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 30px;
        gap: 20px;
    }
    
    .logo-box { text-align: left; min-width: 200px; cursor: pointer; }
    .logo-main {
        font-family: 'Playfair Display', serif;
        font-size: 3rem; 
        font-weight: 700;
        color: #000;
        line-height: 1;
        letter-spacing: -1px;
    }
    .logo-tagline {
        font-family: 'Lato', sans-serif;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #666;
        margin-top: 5px;
    }

    /* SEARCH BAR */
    div[data-testid="stSelectbox"] > div > div {
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 0;
        box-shadow: none;
    }

    /* --- BOOK CARDS (FIXED: NO WHITE BOX) --- */
        /* --- BOOK CARDS (IMPROVED: LESS WHITE SPACE, BIGGER IMAGES) --- */
    .book-card {
    # background: #FEFDFB; /* Trắng kem nhẹ - phù hợp với nền #F9F8F6 */
    padding: 18px;
    border-radius: 12px; /* Bo góc lớn hơn cho premium */
    margin-bottom: 30px;
    position: relative;
    text-align: left;
    display: flex;
    flex-direction: column;
    height: auto;
    min-height: 0;
    
    /* ⭐ ĐỔ BÓNG PREMIUM (3 lớp - magazine style) ⭐ */
    box-shadow: 
        0 1px 3px rgba(0, 0, 0, 0.02),    /* Bóng mờ nền nhẹ */
        0 4px 16px rgba(0, 0, 0, 0.04),   /* Bóng chính */
        0 8px 32px rgba(0, 0, 0, 0.03);   /* Bóng lan tỏa */
    
    /* ⭐ VIỀN TINH TẾ ⭐ */
    border: 1px solid rgba(255, 255, 255, 0.8); /* Viền trắng bên trong */
    outline: 1px solid rgba(0, 0, 0, 0.03);     /* Viền tối bên ngoài */
    
    /* ⭐ HIỆU ỨNG CHUYỂN ĐỘNG PREMIUM ⭐ */
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1); /* Easing mượt */
    
    /* ⭐ GRADIENT BACKGROUND TINH TẾ (tùy chọn) ⭐ */
    background: linear-gradient(
        145deg, 
        FFFFFF 0%,        /* Trắng tinh ở góc */
        FEFDFB 30%,       /* Kem nhẹ ở giữa */
        FDFCFA 100%       /* Kem đậm hơn ở đáy */
    );
}

    .book-card:hover {
        /* ⭐ HIỆU ỨNG HOVER PREMIUM ⭐ */
        transform: translateY(-6px) scale(1.01); /* Nâng và phóng nhẹ */
        
        /* ⭐ BÓNG ĐẬM HƠN KHI HOVER ⭐ */
        box-shadow: 
            0 2px 6px rgba(0, 0, 0, 0.03),
            0 8px 24px rgba(0, 0, 0, 0.06),
            0 16px 48px rgba(0, 0, 0, 0.04);
        
        /* ⭐ VIỀN SÁNG HƠN KHI HOVER ⭐ */
        border-color: rgba(255, 255, 255, 0.95);
        outline-color: rgba(0, 0, 0, 0.05);
        
        /* ⭐ BACKGROUND SÁNG HƠN KHI HOVER ⭐ */
        background: linear-gradient(
            145deg, 
            #FFFFFF 0%,
            #FFFFFF 30%,
            #FEFEFD 100%
        );
    }

    /* ⭐ THÊM HIỆU ỨNG CORNER ACCENT (tùy chọn) ⭐ */
    .book-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, transparent 50%, rgba(0,0,0,0.01) 50%);
        border-radius: 0 12px 0 12px;
        z-index: 1;
    }

    /* ⭐ HIỆU ỨNG FLOATING CHO CONTENT BÊN TRONG ⭐ */
    .book-info {
        position: relative;
        z-index: 2; /* Đặt trên accent corner */
    }

    /* ⭐ HOẶC MÀU NỀN ĐƠN GIẢN HƠN (nếu không thích gradient) ⭐ */
    /*
    .book-card {
        background: #FEFDFC;  // Màu kem trắng nhẹ nhất
    }
    */
    
    # .book-img {
    #     width: 250%;
    #     height: 400px; /* Tăng chiều cao lên để ảnh lớn hơn */
    #     object-fit: contain; /* Giữ nguyên tỷ lệ ảnh */
    #     display: block;
    #     border-radius: 4px;
    #     box-shadow: 5px 5px 15px rgba(0,0,0,0.15);
    #     margin-bottom: 12px; /* Giảm từ 15px xuống 12px */
    #     transition: transform 0.3s ease;
    #     background-color: #f8f8f8; /* Nền nhẹ cho ảnh trắng */
    #     padding: 8px; /* Thêm padding để ảnh không chạm viền */
    # }
    # .book-img:hover {
    #     transform: translateY(-3px);
    #     box-shadow: 8px 8px 20px rgba(0,0,0,0.2);
    # }
    /* Ảnh sách đã được xử lý viền trắng */
    .book-img-cropped {
    width: 160px !important;        /* CHỈNH WIDTH Ở ĐÂY */
    height: 250px !important;       /* CHỈNH HEIGHT Ở ĐÂY */
    object-fit: cover !important;   /* QUAN TRỌNG: cover sẽ crop ảnh */
    object-position: center center !important; /* Căn vào giữa */
    display: block;
    border-radius: 6px;
    margin: 0 auto 12px auto;       /* Căn giữa ảnh */
    
    /* Hiệu ứng */
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    border: 1px solid #e0e0e0;
    background-color: white;        /* Nền trắng thay cho viền trắng của ảnh */
    
    /* TRANSFORM để zoom vào ảnh (crop ảnh) */
    transform: scale(0.9);          /* CHỈNH SCALE Ở ĐÂY: 1.1 = zoom 10% */
    
    /* Giới hạn kích thước thực tế */
    max-width: 100%;
    max-height: 100%;
}

    # .book-img-cropped:hover {
    #     transform: scale(1.15) translateY(-4px); /* Zoom thêm khi hover */
    #     box-shadow: 0 8px 24px rgba(0,0,0,0.2);
    # }
    .book-info {
        padding: 0;
        margin-top: 8px; /* Giảm từ 10px xuống 8px */
        flex-grow: 0; /* Không cho phần info chiếm thêm không gian */
    }
    .book-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.05rem; /* Giữ nguyên hoặc giảm nhẹ */
        font-weight: 600;
        line-height: 1.3;
        margin-bottom: 6px; /* Giảm từ 5px xuống còn 6px (tăng nhẹ cho cân đối) */
        color: #000;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        min-height: 2.6em; /* Chiều cao tối thiểu cho 2 dòng */
    }
    .book-price {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    color: #27ae60; /* Xanh lá nhẹ nhàng */
    font-size: 1.05rem;
    letter-spacing: 0.5px;
    margin-top: 5px;
    display: inline-flex;
    align-items: center;
    padding: 2px 8px;
    background: rgba(39, 174, 96, 0.08);
    border-radius: 4px;
    border-left: 3px solid #27ae60;
}
                /* Adjust column spacing for better layout */
    div[data-testid="column"] {
        padding-left: 12px !important;
        padding-right: 12px !important;
    }

    /* --- SIDEBAR RECS --- */
    .rec-card {
        display: flex;
        gap: 15px;
        margin-bottom: 25px;
        align-items: flex-start;
    }
    .rec-img {
        width: 70px; /* Ảnh rec to hơn chút */
        aspect-ratio: 2/3;
        object-fit: cover;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.15);
    }
    .rec-title {
        font-family: 'Playfair Display', serif;
        font-size: 1rem;
        font-weight: 600;
        line-height: 1.2;
        margin-bottom: 5px;
    }
    .rec-match {
        font-size: 0.7rem;
        color: #999;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* BUTTONS STYLE UPGRADE */
    div.stButton > button {
        border-radius: 0;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1px;
        font-size: 0.75rem;
        padding: 10px 20px;
        transition: 0.2s;
        border: 1px solid #000;
        background-color: transparent;
        color: #000;
    }
    div.stButton > button:hover {
        background-color: #000;
        color: white;
        border-color: #000;
    }
    
    /* Primary Action Override */
    div.stButton > button:active, div.stButton > button:focus {
        background-color: #000;
        color: white;
        border-color: #000;
    }

</style>
""", unsafe_allow_html=True)

# --- 3. DATA & LOGIC ---

@st.cache_data
def load_data():
    meta = pd.read_csv('books_metadata.csv')
    rules = pd.read_csv('rules_final.csv')
    return meta, rules

try:
    books_df, rules_df = load_data()
except:
    st.error("⚠️ Data files not found.")
    st.stop()

def get_image(title):
    row = books_df[books_df['original_title'] == title]
    if not row.empty:
        url = row.iloc[0]['image_url']
        if "nophoto" in str(url) or pd.isna(url):
            return "https://via.placeholder.com/300x450.png?text=No+Cover"
        return url
    return "https://via.placeholder.com/300x450.png?text=404"

def get_price(title):
    row = books_df[books_df['original_title'] == title]
    return row.iloc[0]['price'] if not row.empty else 0

def add_to_cart_callback(book_title):
    # Logic thêm vào giỏ
    if book_title not in st.session_state.cart:
        st.session_state.cart.append(book_title)
        st.toast(f"Added to bag: {book_title}", icon="👜")
    else:
        st.toast(f"Already in bag", icon="🕊️")

def remove_from_cart(book):
    if book in st.session_state.cart:
        st.session_state.cart.remove(book)
        st.rerun()

def clear_cart():
    st.session_state.cart = []
    st.rerun()

def get_recommendations():
    if not st.session_state.cart: return []
    cart_set = set(st.session_state.cart)
    recs = []
    for _, row in rules_df.iterrows():
        ant = set([x.strip() for x in row['antecedents'].split(',')])
        if ant.issubset(cart_set):
            cons = row['consequents']
            if cons not in st.session_state.cart:
                if not any(r['book'] == cons for r in recs):
                    recs.append({'book': cons, 'conf': row['confidence']})
    recs.sort(key=lambda x: x['conf'], reverse=True)
    return recs[:5]

# --- 4. NAVIGATION & HEADER ---
def go_home(): st.session_state.page = 'home'
def go_cart(): st.session_state.page = 'cart'

def render_header():
    # Sử dụng columns để căn chỉnh Layout
    c1, c2, c3 = st.columns([1.5, 3, 1], vertical_alignment="center")
    
    with c1:
        st.markdown(f"""
        <div class="logo-box" onclick="window.location.reload()">
            <div class="logo-main">📚Bookies.</div>
            <div class="logo-tagline">The Premium Collection</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        all_titles = books_df['original_title'].tolist()
        search_selection = st.selectbox(
            "Search",
            options=all_titles,
            index=None,
            placeholder="🔎Search for titles, authors...",
            label_visibility="collapsed",
            key="main_search"
        )

    with c3:
        # Lấy số lượng từ session_state trực tiếp để đảm bảo luôn đúng
        cart_count = len(st.session_state.cart)
        if st.button(f"🛒YOUR BAG ({cart_count})", use_container_width=True):
            go_cart()
            st.rerun()
    
    st.markdown("---")
    return search_selection

# --- 5. PAGE CONTENT ---

search_res = render_header()

# === PAGE: HOME ===
if st.session_state.page == 'home':
    
    col_left, col_right = st.columns([1, 3], gap="large")

    # --- LEFT COLUMN: RECOMMENDATIONS ---
    with col_left:
        st.markdown("### For You")
        st.caption("Curated picks based on your taste.")
        st.write("") 

        recs = get_recommendations()
        
        if recs:
            for item in recs:
                b_title = item['book']
                b_img = get_image(b_title)
                match_score = int(item['conf']*100)
                
                # Render Sidebar Recs
                st.markdown(f"""
                <div class="rec-card">
                    <img src="{b_img}" class="rec-img">
                    <div class="rec-info">
                        <div class="rec-title">{b_title}</div>
                        <div class="rec-match">Match {match_score}%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Nút ADD dùng callback để update số lượng ngay
                if st.button("ADD", key=f"add_rec_{b_title}"):
                    add_to_cart_callback(b_title)
                    # Force update UI trick (nếu cần thiết, nhưng callback thường tự xử lý)
                    time.sleep(0.1) 
                    st.rerun()
        else:
            if not st.session_state.cart:
                st.info("Start adding books to unlock recommendations.")
            else:
                st.write("Explore our collection to find more.")

    # --- RIGHT COLUMN: CATALOG ---
    with col_right:
        if search_res:
            st.markdown(f"### Results for: *{search_res}*")
            display_books = books_df[books_df['original_title'] == search_res]
        else:
            st.markdown("### The Collection")
            display_books = books_df.head(12) 

        if display_books.empty:
            st.warning("No books found.")
        
        books_list = display_books.to_dict('records')
        chunks = [books_list[i:i + 3] for i in range(0, len(books_list), 3)]

        for chunk in chunks:
            cols = st.columns(3)
            for i, book in enumerate(chunk):
                with cols[i]:
                    img = get_image(book['original_title'])
                    price = book['price']
                    title = book['original_title']
                    
                    # HTML Card (Đã bỏ khung trắng, ảnh tràn viền)
                    st.markdown(f"""
                    <div class="book-card">
                        <img src="{img}" class="book-img-cropped">
                        <div class="book-info">
                            <div class="book-title" title="{title}">{title}</div>
                            <div class="book-price">${price}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Button ADD
                    st.button(
                        "ADD TO BAG", 
                        key=f"add_main_{title}_{random.randint(0,9999)}", 
                        on_click=add_to_cart_callback, 
                        args=(title,), 
                        use_container_width=True
                    )
            
            st.write("") 

# === PAGE: SHOPPING BAG (CART) ===
elif st.session_state.page == 'cart':
    st.markdown("## Your Shopping Bag")
    
    # Action Buttons Bar (Mới thêm)
    col_actions_1, col_actions_2 = st.columns([1, 4])
    with col_actions_1:
        if st.button("← CONTINUE SHOPPING"):
            go_home()
            st.rerun()
    with col_actions_2:
        # Nút Remove All (chỉ hiện khi có đồ)
        if st.session_state.cart:
             if st.button("REMOVE ALL ITEMS"):
                 clear_cart()

    st.divider()

    c1, c2 = st.columns([2, 1], gap="large")
    
    with c1:
        if st.session_state.cart:
            for item in st.session_state.cart:
                p = get_price(item)
                cc1, cc2, cc3 = st.columns([1, 3, 1])
                with cc1:
                    st.image(get_image(item), width=80)
                with cc2:
                    st.markdown(f"<div style='font-family:Playfair Display; font-size:1.1rem; font-weight:bold'>{item}</div>", unsafe_allow_html=True)
                    st.write(f"${p}")
                with cc3:
                    st.write("")
                    if st.button("Remove", key=f"del_{item}"):
                        remove_from_cart(item)
                st.divider()
        else:
            st.info("Your bag is empty.")

    with c2:
        if st.session_state.cart:
            total = sum([get_price(x) for x in st.session_state.cart])
            st.markdown(f"""
            <div style="background-color: white; padding: 30px; border: 1px solid #eee;">
                <h4 style="margin-top:0; font-style:italic">Order Summary</h4>
                <div style="display:flex; justify-content:space-between; margin-bottom:15px; font-size: 0.9rem;">
                    <span>Subtotal</span>
                    <span>${total}</span>
                </div>
                 <div style="display:flex; justify-content:space-between; margin-bottom:20px; font-size: 0.9rem; color:#666;">
                    <span>Shipping</span>
                    <span>Calculated at checkout</span>
                </div>
                <hr style="border-top: 1px solid #ddd;">
                <div style="display:flex; justify-content:space-between; font-weight:bold; font-size:1.3rem; margin-top:15px;">
                    <span>Total</span>
                    <span>${total}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            if st.button("CHECKOUT", type="primary", use_container_width=True):
                st.balloons()
                st.success("Order placed successfully!")
                time.sleep(2)
                st.session_state.cart = []
                go_home()
                st.rerun()

# --- FOOTER ---
st.write("")
st.write("")
st.markdown("<div style='text-align:center; color:#888; font-size:0.75rem; margin-top:50px; border-top:1px solid #e0e0e0; padding-top:30px; letter-spacing:1px'>© 2025 BOOKIES PREMIUM. THE EDITORIAL COLLECTION.</div>", unsafe_allow_html=True)