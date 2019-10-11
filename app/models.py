from app import db

class LeaderboardEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Entry Metadata
    name = db.Column(db.String(64), index=True, unique=True)
    is_pretrained = db.Column(db.Boolean, index=True)
    is_neural = db.Column(db.Boolean, index=True)
    submission_date = db.Column(db.Date, index=True)
    institution = db.Column(db.String(64), index=True)
    citation = db.Column(db.String(256))
    # Secondary Structure
    ss_cb513_3 = db.Column(db.Float, index=True)
    ss_ts115_3 = db.Column(db.Float, index=True)
    ss_casp12_3 = db.Column(db.Float, index=True)
    ss_cb513_8 = db.Column(db.Float, index=True)
    ss_ts115_8 = db.Column(db.Float, index=True)
    ss_casp12_8 = db.Column(db.Float, index=True)
    # Contact Prediction
    cp_medium_long_pl5 = db.Column(db.Float, index=True)
    cp_short_range_auprc = db.Column(db.Float, index=True)
    cp_short_range_pl = db.Column(db.Float, index=True)
    cp_short_range_pl2 = db.Column(db.Float, index=True)
    cp_short_range_pl5 = db.Column(db.Float, index=True)
    cp_medium_range_auprc = db.Column(db.Float, index=True)
    cp_medium_range_pl = db.Column(db.Float, index=True)
    cp_medium_range_pl2 = db.Column(db.Float, index=True)
    cp_medium_range_pl5 = db.Column(db.Float, index=True)
    cp_long_range_auprc = db.Column(db.Float, index=True)
    cp_long_range_pl = db.Column(db.Float, index=True)
    cp_long_range_pl2 = db.Column(db.Float, index=True)
    cp_long_range_pl5 = db.Column(db.Float, index=True)
    # Remote Homology
    rh_fold_1 = db.Column(db.Float, index=True)
    rh_fold_5 = db.Column(db.Float, index=True)
    rh_superfamily_1 = db.Column(db.Float, index=True)
    rh_superfamily_5 = db.Column(db.Float, index=True)
    rh_family_1 = db.Column(db.Float, index=True)
    rh_family_5 = db.Column(db.Float, index=True)
    # Fluorescence
    fl_mse_full = db.Column(db.Float, index=True)
    fl_rho_full = db.Column(db.Float, index=True)
    fl_mse_bright = db.Column(db.Float, index=True)
    fl_rho_bright = db.Column(db.Float, index=True)
    fl_mse_dark = db.Column(db.Float, index=True)
    fl_rho_dark = db.Column(db.Float, index=True)
    # Stability
    st_rho = db.Column(db.Float, index=True)
    st_acc = db.Column(db.Float, index=True)
    st_aaa_rho = db.Column(db.Float, index=True)
    st_aaa_acc = db.Column(db.Float, index=True)
    st_abba_rho = db.Column(db.Float, index=True)
    st_abba_acc = db.Column(db.Float, index=True)
    st_babb_rho = db.Column(db.Float, index=True)
    st_babb_acc = db.Column(db.Float, index=True)
    st_bbabb_rho = db.Column(db.Float, index=True)
    st_bbabb_acc = db.Column(db.Float, index=True)

    def __repr__(self) -> str:
        return f'<Entry for model {self.name}>'


class DisplayName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key_name = db.Column(db.String(256))
    display_name = db.Column(db.String(256))

    def __repr__(self) -> str:
        return f'<Maps {self.key_name} => {self.display_name}>'

    def get_display_name(self, key_name: str) -> str:
        pass
